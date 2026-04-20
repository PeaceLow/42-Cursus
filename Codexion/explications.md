# Explications Détaillées du Fonctionnement du Code

Ce projet est une adaptation du célèbre problème algorithmique des **Philosophes Dînants** (Dining Philosophers), transposé dans l'univers de la programmation.
Ici, les "philosophes" sont des **Programmeurs (Coders)**, les "fourchettes" sont des **Clés USB (Dongles)**, et leurs actions consistent à *compiler*, *déboguer* et *refactoriser* (au lieu de *manger*, *dormir* et *penser*). S'ils ne compilent pas assez vite, ils font un **burnout** (meurent). De plus, un système d'ordonnancement poussé (Scheduler FIFO ou EDF - Earliest Deadline First) est mis en place pour gérer l'acquisition des clés.

## 1. Structures Principales (`struct.h`)

Le fonctionnement du programme tourne autour de trois structures majeures :

- **`t_env`** : L'environnement global.
  - Il contient les arguments de la simulation : `nb_coders`, temps pour burnout, compiler, déboguer, refactoriser, nombre de compilations requises, etc.
  - Il abrite le tableau global de dongles (`dongles`), l'heure de démarrage globale (`start_time`), et un marqueur (`stop_sim`) pour indiquer quand tout doit s'arrêter de façon sécurisée via l'utilisation de **mutex** (`print_lock`, `stop_lock`).

- **`t_dongle`** : Représente une ressource partagée.
  - Possède un `pthread_mutex_t mutex` qui assure qu'un seul codeur utilise ce dongle à la fois.
  - Intègre une file d'attente (`queue`) et un pointeur vers sa propre politique de gestion (`queue_lock`, `available_at`) pour l'ordonnancement des requêtes via des variables de condition (ex: `cond`).

- **`t_request`** : Requête individuelle d'un codeur pour accéder à un dongle. 
  - Trace le moment d'arrivée et la "deadline" pour prioriser l'accès lors de l'utilisation d'EDF.

- **`t_coder`** : L'unité de traitement autonome (un thread par codeur).
  - Détient un ID, son nombre de compilations réalisées (`nb_compiles`), ses pointeurs vers les dongles adjacents (`left_dongle`, `right_dongle`), et un identifiant de thread (`pthread_t thread`).

## 2. Déroulement du Programme

### A. Initialisation (`init.c` & `main.c`)
On parse les arguments puis `init_env` initie l'environnement.
Les dongles (ressources) et toutes les structures de synchronisation associées (mutex, cond) sont allouées et initialisées.
`init_coders` donne à chaque codeur deux pointeurs vers les dongles qu'il doit emprunter (gauche, droite).

### B. Création des Threads (`main.c`)
La fonction `start_threads` crée simultanément :
1. **Un thread de supervision (Monitor)** via `monitor_routine` qui vérifiera constamment si quelqu'un a fait un burnout ou si la simulation est terminée.
2. **Un thread par Codeur** exécutant `coder_routine`, où vivent les requêtes concurrentielles.

### C. La Routine du Codeur (`routine.c`)
Tant que la simulation n'est pas arrêtée :
1. **Prise des Dongles (`take_dongles`)** : Le codeur tente de saisir les requêtes de ses clés. Pour éviter les Deadlocks, on demande toujours celui ayant l'ID le plus petit en premier.
2. **Compiler** : S'il obtient les deux, il met à jour sa trace chronologique (`last_compile_start`), compile un certain temps (`usleep` encapsulé).
3. **Libérer les Dongles (`release_dongles`)** : Il remet les clés à disposition ce qui permet de réveiller via des signaux le codeur suivant dans la file d'attente d'accès au dongle. 
4. **Débogue & Refactorisation** : Il se met ensuite en pause pour de courtes durées pour simuler l'avancement. 

### D. L'ordonnanceur - Scheduler (`scheduler.c`)
Lorsqu'un codeur veut un dongle :
- Il s'ajoute à la `queue` du dongle concerné (avec son deadline et moment d'arrivée).
- Il boucle et bloque sur un `pthread_cond_wait()` tant que :
  - Le dongle est en `cooldown`.
  - Ce n'est pas à son tour, déterminé par la fonction `find_next()` (qui priorise selon `FIFO` ou `EDF`).
- À sa libération, le dongle signale le *prochain* processus éligible (`pthread_cond_signal`).

### E. Le Moniteur de Suivi (`monitor.c`)
Ce thread séparé tourne en permanence sans utiliser de ressources actives (`usleep(1000)`).
- Il vérifie en boucle `check_burnout` : si le timestamp récent prouve que le codeur a dépassé son `time_to_burnout` depuis sa dernière exécution passée, ce thread avertit le reste du programme pour déclarer l'arrêt (`stop_sim`).
- Il observe si tous les codeurs ont respecté l'objectif de compilation requis (`nb_compiles_required`).

## 3. Explication des Fonctions Pthread Utilisées

Les threads POSIX (pthreads) sont fondamentaux pour créer du comportement asynchrone et manipuler la concurrence dans l'application C de cet exercice. 

- **`pthread_create(pthread_t *thread, const pthread_attr_t *attr, void *(*start_routine) (void *), void *arg)`**
  - **Où** : Lors de la création de `monitor_routine` et `coder_routine`.
  - **Rôle** : Démarre l'exécution indépendante en créant un nouveau thread. Appelle formellement la fonction pointée (ici un moniteur ou la routine d'un programmeur concurrentiel) et lui permet d'évoluer en parallèle de la base originelle de la boucle principale `main`. 

- **`pthread_join(pthread_t thread, void **retval)`**
  - **Où** : Appelé dans `wait_and_cleanup()`.
  - **Rôle** : Demande d'attendre docilement la fin formelle de l'exécution complète des threads ciblés par leur ID (monitor et chaque coder) afin d'assurer l'achèvement de toute mutation et d'empêcher le `main` de terminer prématurément, provoquant la destruction de la mémoire active.

- **`pthread_mutex_init(pthread_mutex_t *mutex, const pthread_mutexattr_t *attr)`** & **`pthread_mutex_destroy`**
  - **Où** : Utilisé dans `init.c` et `cleanup`.
  - **Rôle** : Les "mutex" (Mutual Exclusions) agissent en système de verrou global ou local (ex: protéger les terminaux d'affichage via `print_lock` ou les états limités comme `stop_lock` et des `dongle->mutex`). Détruit ces verrous ensuite pour rendre les ressources à la machine.

- **`pthread_mutex_lock(pthread_mutex_t *mutex)`** & **`pthread_mutex_unlock`**
  - **Où** : Partout (`log_status`, `scheduler.c`, `routine.c`).
  - **Rôle** : Forme la barrière d'anti-collision de race. Si un Thread "A" arrive ici et s'empare du "lock", les autres threads (le moniteur de statut ou les autres codeurs) voulant utiliser cette portion de code seront bloqués en latence jusqu'à ce que "A" franchisse explicitement un "unlock". 

- **`pthread_cond_init(pthread_cond_t *cond, attr)`** & **`pthread_cond_destroy`**
  - **Où** : Dans le code des Dongles (Files d'attentes individualisées).
  - **Rôle** : Variables d'état conditionnel (Condition Variables) créées pour être associées spécifiquement à chaque `mutex_queue`. 

- **`pthread_cond_wait(pthread_cond_t *cond, pthread_mutex_t *mutex)`**
  - **Où** : Dans `wait_dongle` du *scheduler.c*.
  - **Rôle** : Met volontairement un thread de codeur dans un état passif prolongé sans gaspiller d'usage CPU "busy-wait" tant qu'il ne détient pas la priorité de passage pour réserver un dongle. Il libére simultanément son `queue_lock` pendant que la latence persiste.

- **`pthread_cond_signal(pthread_cond_t *cond)`**
  - **Où** : À l'intérieur de `dongle_release` du *scheduler*.
  - **Rôle** : Soustrait l'ordre actif libérant au `cond` de l'ordinateur suivant. Lorsqu'une clé USB est libérée, ce processus informe sélectivement une file d'attente (soit `FIFO` de suite, soit l'`EDF` par temps d'arrivée) dont le tour vient d'arriver pour qu'il sorte de son état somnoparent généré par `pthread_cond_wait`.
