This project has been created as part of the 42 curriculum by zakburak, avauclai.

# Push_swap

**Projet réalisé dans le cadre du cursus 42 par zakburak & avauclai**

---

## 📋 Description

**Push_swap** est un projet algorithmique dont l'objectif est de trier une pile de nombres en utilisant un ensemble limité d'instructions. Le défi consiste à manipuler deux piles (A et B) et à trouver la stratégie la plus efficace pour minimiser le nombre d'opérations.

Ce projet permet de développer :
- Une solide compréhension des algorithmes de tri
- La maîtrise de la complexité algorithmique
- L'optimisation et la logique de programmation

---

## 🚀 Utilisation

### Compilation
```bash
make
```

### Exécution
```bash
./push_swap <liste de nombres>
```

**Exemple :**
```bash
./push_swap 5 8 2 9 1
```

---

## ⚙️ Options disponibles

| Option | Description |
|--------|-------------|
| `--bench` | Affiche les statistiques d'exécution (disorder, stratégie, nombre d'opérations) |
| `--simple` | Force l'utilisation de l'algorithme simple (Selection Sort) |
| `--medium` | Force l'utilisation de l'algorithme medium (Chunk Sort) |
| `--complex` | Force l'utilisation de l'algorithme complexe (Quick Sort) |
| `--adaptive` | Sélectionne automatiquement le meilleur algorithme (par défaut) |

**Exemples :**
```bash
./push_swap --bench 5 8 2 9 1
./push_swap --medium 42 21 10 5 1
./push_swap --bench --simple 5 8 2 9 1
```

---

## 🧪 Commandes de test

### Tests rapides
```bash
# Test avec 100 nombres
shuf -i 0-9999 -n 100 | xargs ./push_swap --bench

# Test avec 500 nombres
shuf -i 0-9999 -n 500 | xargs ./push_swap --bench
```

### Tester Python
Un tester Python est inclus dans le projet pour des tests plus approfondis.

### Bonus (Checker)
```bash
make bonus
```

---

## 🧠 Algorithmes implémentés

### 1. **Selection Sort** - Simple `O(n²)`
Algorithme adapté aux petites piles (≤ 5 éléments).

**Principe :** À chaque itération, on sélectionne le plus petit élément de la pile A et on le pousse dans la pile B, puis on repousse tout dans A dans l'ordre.

**Avantage :** Simple à implémenter et efficace pour les très petites listes.

---

### 2. **Chunk Sort** - Medium `O(n√n)`
Algorithme optimisé pour les piles de taille moyenne (50-500 éléments).

**Principe :**
- Conversion des valeurs en rangs (0, 1, 2, ..., n-1)
- Division en "chunks" (zones de valeurs)
- Envoi des éléments vers la pile B par chunks, en optimisant les rotations
- Rapatriement des éléments dans l'ordre (du plus grand au plus petit)

**Avantage :** Réduit significativement le nombre d'opérations par rapport au tri simple.

---

### 3. **Quick Sort** - Complex `O(n log n)`
Algorithme le plus performant pour les grandes piles (500+ éléments).

**Principe :**
- Sélection d'un pivot (médiane des valeurs)
- Partitionnement : éléments < pivot → pile B, éléments ≥ pivot → rotations dans A
- Récursion sur les sous-ensembles jusqu'à obtenir des piles triées
- Utilisation des deux piles de manière optimale

**Avantage :** Complexité logarithmique, idéal pour les grandes listes.

---

### 4. **Adaptive** - Adaptatif `O(n)` à `O(n log n)`
Mode par défaut qui sélectionne automatiquement le meilleur algorithme selon :
- La taille de la pile
- Le niveau de désordre (disorder ratio)

**Stratégie :**
- ≤ 3 éléments → Tri direct optimisé
- ≤ 5 éléments → Selection Sort
- Disorder < 20% → Selection Sort
- Disorder < 50% → Chunk Sort
- Sinon → Quick Sort

---

## 📚 Ressources

- Documentation sur Medium
- Recherches et optimisations avec ChatGPT
- Analyse des algorithmes de tri classiques adaptés aux contraintes du projet

---

## 📊 Performances attendues

| Taille | Algorithme recommandé | Opérations attendues |
|--------|---------------------- |----------------------|
|   3    |       Adaptatif       |         ≤ 3          |
|   5    |       Adaptatif       |         ≤ 12         |
|  100   |       Chunk Sort      |         < 700        |
|  500   |       Quick Sort      |         < 5500       |

---

## 👥 Auteurs

- **zakburak**
- **avauclai**

*Projet 42 - 2025/2026*
