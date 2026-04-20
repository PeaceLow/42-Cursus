*This project has been created as part of the 42 curriculum by avauclai*

# Codexion

Simulation multithreadée inspirée du problème des philosophes, où des **codeurs** partagent des **dongles** (ressources critiques) pour compiler du code. Chaque codeur doit alterner entre : prendre les dongles → compiler → déboguer → refactorer → recommencer. Un codeur qui ne commence pas une nouvelle compilation à temps **fait un burnout**.

---

## Compilation

```bash
make
```

---

## Utilisation

```bash
./codexion nb_coders burnout compile debug refactor nb_compiles cooldown scheduler
```

| Argument       | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `nb_coders`    | Nombre de codeurs (threads)                                                 |
| `burnout`      | Temps maximal (ms) entre deux débuts de compilation avant burnout           |
| `compile`      | Durée (ms) d'une phase de compilation                                       |
| `debug`        | Durée (ms) d'une phase de débogage                                         |
| `refactor`     | Durée (ms) d'une phase de refactoring                                       |
| `nb_compiles`  | Nombre de compilations requises pour terminer (0 = infini, jusqu'au burnout)|
| `cooldown`     | Temps (ms) d'indisponibilité d'un dongle après sa libération                |
| `scheduler`    | Algorithme d'ordonnancement : `fifo` ou `edf`                               |

---

## Cycle d'un codeur

```
[prendre les dongles] → is compiling → [libérer les dongles] → is debugging → is refactoring → (répéter)
```

Le **burnout** est déclenché si le temps écoulé depuis le dernier début de compilation dépasse `burnout` ms.

---

## Tests

### Test 1 — Cycle nominal, aucun burnout (FIFO)

```bash
./codexion 4 410 200 100 100 0 0 fifo
```

**Paramètres :** 4 codeurs, burnout à 410 ms, cycle complet = 400 ms (200 compile + 100 debug + 100 refactor), pas de limite de compilations, sans cooldown.

**Résultat attendu :**
- Le cycle complet (400 ms) est inférieur au délai de burnout (410 ms) : **aucun burnout ne doit survenir**.
- La simulation tourne indéfiniment, chaque codeur compilant en boucle sans jamais dépasser le seuil.
- Pour arrêter la simulation, utiliser `Ctrl+C`.

```
0 1 is compiling
0 2 is compiling
0 3 is compiling
0 4 is compiling
200 1 is debugging
200 2 is debugging
...
(tourne indéfiniment sans burnout)
```

---

### Test 2 — Burnout inévitable, cycle trop long

```bash
./codexion 3 310 200 100 100 0 0 fifo
```

**Paramètres :** 3 codeurs, burnout à 310 ms, cycle = 400 ms.

**Résultat attendu :**
- Le cycle complet (400 ms) dépasse le délai de burnout (310 ms).
- Chaque codeur compile une fois (~200 ms), débogue (~100 ms, total ~300 ms), puis le monitor détecte le burnout à **310 ms** pendant la phase de débogage ou de refactoring.
- La simulation se termine très rapidement (~310 ms) avec un `burned out`.

```
0 1 is compiling
0 2 is compiling
0 3 is compiling
200 1 is debugging
...
310 2 burned out
```

---

### Test 3 — Nombre de compilations requis avec burnout

```bash
./codexion 5 800 200 100 100 5 0 fifo
```

**Paramètres :** 5 codeurs, burnout à 800 ms, cycle = 400 ms, 5 compilations requises par codeur.

**Résultat attendu :**
- Atteindre 5 compilations nécessiterait ~2000 ms par codeur (5 × 400 ms), bien au-delà du burnout de 800 ms.
- Chaque codeur peut effectuer environ **2 compilations** avant que le burnout ne survienne (2 × 400 ms = 800 ms).
- La contention entre 5 codeurs pour 5 dongles en FIFO aggrave la situation pour les codeurs moins prioritaires.
- La simulation se termine par un `burned out` avant que tous aient atteint 5 compilations.

```
0 1 is compiling
...
800 4 burned out
```

---

### Test 4 — Cooldown de dongle (blocage de ressource)

```bash
./codexion 2 400 100 100 100 0 150 fifo
```

**Paramètres :** 2 codeurs, burnout à 400 ms, cycle = 300 ms, cooldown de 150 ms sur chaque dongle.

**Résultat attendu :**
- Sans cooldown, un cycle durerait 300 ms < 400 ms → les codeurs survivraient.
- Avec un cooldown de 150 ms, après la libération d'un dongle, l'autre codeur doit attendre **150 ms** supplémentaires pour le réutiliser.
- Le cycle effectif devient : 300 ms (cycle) + 150 ms (attente cooldown) = **450 ms > 400 ms** → burnout inévitable.
- La simulation se termine avec un `burned out`.

```
0 1 is compiling
0 2 has taken a dongle
100 1 is debugging
200 1 is refactoring
300 1 has taken a dongle   ← attend le cooldown
400 2 burned out
```

---

### Test 5 — FIFO : risque de famine

```bash
./codexion 4 500 200 100 100 0 0 fifo
```

**Paramètres :** 4 codeurs, burnout à 500 ms, cycle = 400 ms, FIFO.

**Résultat attendu :**
- En FIFO, les codeurs sont servis dans l'ordre d'arrivée dans la file d'attente du dongle.
- Un codeur arrivé légèrement après les autres peut attendre plus longtemps, dépassant ainsi le seuil de burnout.
- La simulation se termine avec **un burnout** sur le(s) codeur(s) désavantagés par l'ordre FIFO.
- Les codeurs qui obtiennent les dongles en premier peuvent effectuer **1 compilation**.

```
0 1 is compiling
0 3 is compiling
...
500 4 burned out
```

---

### Test 6 — EDF : meilleure équité

```bash
./codexion 4 500 200 100 100 0 0 edf
```

**Paramètres :** identiques au Test 5, mais avec l'ordonnanceur **EDF** (Earliest Deadline First).

**Résultat attendu :**
- En EDF, la priorité est donnée au codeur dont la deadline (temps restant avant burnout) est la plus proche.
- La ressource est mieux distribuée : un codeur proche du burnout sera servi avant un codeur ayant encore du temps.
- La simulation dure **plus longtemps** qu'en FIFO avant qu'un burnout survienne.
- Idéalement, tous les codeurs effectuent **1 compilation** équitablement avant que le burnout survienne sur tous simultanément.

```
0 1 is compiling
0 2 is compiling
0 3 is compiling
0 4 is compiling
200 1 is debugging
...
500 1 burned out   ← plus tard qu'en FIFO
```

---

## Comparaison FIFO vs EDF

| Critère                    | FIFO                              | EDF                                   |
|----------------------------|-----------------------------------|---------------------------------------|
| Ordre de service           | Premier arrivé, premier servi     | Deadline la plus proche en priorité   |
| Équité                     | Faible (famine possible)          | Élevée (priorise les plus urgents)    |
| Risque de burnout précoce  | Élevé pour les derniers arrivés   | Réduit, tous ont une chance équitable |
| Cas idéal                  | Si tous les codeurs sont synchrones| Si les deadlines varient              |

---

## Nettoyage

```bash
make clean    # Supprime les fichiers objets
make fclean   # Supprime les objets et l'exécutable
make re       # Recompile tout depuis zéro
```
