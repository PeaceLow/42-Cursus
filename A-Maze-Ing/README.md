*This project has been created as part of the 42 curriculum by zakburak, avauclai.*

# A-Maze-Ing : Générateur et Solveur de Labyrinthes

## Description
A-Maze-Ing est un projet de génération procédurale, de résolution et d'affichage interactif de labyrinthes complexes. Son but est d'explorer différents algorithmes de génération (labyrinthes parfaits ou imparfaits) ainsi que des méthodes de recherche de chemin (pathfinding). Le programme inclut une visualisation ASCII détaillée, animée et paramétrable.

## Instructions
### Compilation et Installation
Le projet est écrit en Python. La commande `make install` créera automatiquement l'environnement virtuel et y installera toutes les dépendances :
```bash
make install
```

### Exécution
Vous pouvez exécuter le programme directement ou utiliser le Makefile :
```bash
python3 a_maze_ing.py config.txt
# ou
make run
```

## Ressources
- **Références :** Articles Wikipédia sur les algorithmes de Prim, de Kruskal et le parcours en profondeur/largeur (DFS/BFS).
- **Intelligence Artificielle :** Gemini ou GitHub Copilot ont été utilisés pour la rédaction docstrings, la recherche de patterns d'architecture et l'assistance sur la coloration ASCII dans le terminal. L'implémentation de l'algo de base reste entièrement d'origine humaine.

## Configuration (`config.txt`)
Le fichier de configuration structure l'ensemble du comportement du générateur et de l'affichage. Chaque ligne définit une paire `Clé=Valeur`.
- `WIDTH` / `HEIGHT` : Dimensions de la grille du labyrinthe.
- `ENTRY` / `EXIT` : Coordonnées de l'entrée et de la sortie (ex: `0,0`).
- `OUTPUT_FILE` : Nom du fichier de destination (ex: `maze.txt`).
- `PERFECT` : `True` pour un labyrinthe sans boucles, `False` pour permettre des boucles.
- `LOG_LEVEL` : Niveau de journalisation (`DEBUG`, `INFO`, `WARNING`, `ERROR`).
- `DISPLAY` : Mode d'affichage (ex: `ASCII`).
- `SEED` : Graine aléatoire garantissant la reproductibilité d'un labyrinthe.
- `ANIMATION` : Active l'animation en temps réel de la génération/résolution (`True`/`False`).
- `MAZE_STYLE` : Visuel des murs (`fin`, `epais`, `massif`).
- `WALL_COLOR`, `ENTRY_COLOR`, `EXIT_COLOR`, etc. : Codes de couleur (1 à 10) pour les différents éléments.
- `GENERATOR` : Algorithme utilisé pour la génération (`PRIM`, `DFS`, `KRUSKAL`).
- `SOLVER` : Algorithme de résolution (`DFS`, `BFS`).

## Algorithme de Génération
L'algorithme de génération par défaut est **PRIM** (implémenté aux côtés de DFS et KRUSKAL).
**Pourquoi ce choix ?**
L'algorithme de Prim aléatoire a été choisi car il génère des labyrinthes visuellement très esthétiques, équilibrés, caractérisés par de nombreuses ramifications courtes (contrairement au DFS qui crée souvent de longs couloirs tortueux). Cela rend les impasses dures à anticiper visuellement.

## Réutilisabilité du Code
La structure de ce projet se veut très modulaire :
- Le module `mazegen_forge` (packaging local contenant `generator.py` et `solver.py`) se comporte comme une bibliothèque autonome pour les algorithmes purs, pouvant être réimporté n'importe où sans dépendre de l'affichage ASCII.
- Le design pattern **Observer** (`utils/observer.py`) a été mis en place pour dissocier complètement la logique d'algorithme de la logique de rendu graphique (`display/`). Ce découplage permet d'utiliser le `core` indépendamment dans d'autres projets.

## Équipe et Gestion de Projet
- **Rôles de chaque membre :**
  - `zakburak` : Intégration des algorithmes de base et de l'architecture global + backend
  - `avauclai` : Rendu graphique ASCII, animations et parsing de la config
- **Planification anticipée et évolution :** Début par l'architecture globale, suivi du moteur de génération, de l'affichage en terminal puis finalement la résolution animée.
- **Ce qui a bien fonctionné / À améliorer :** La séparation backend/frontend a été très efficace. Une amélioration future pourrait inclure l'intégration d'une interface graphique avec MLX.

## Fonctionnalités Avancées
- **Algorithmes Multiples :** Support complet pour la génération avec `PRIM`, `DFS`, `KRUSKAL` et résolution avec `DFS`, `BFS`.
- **Animations ASCII fluides intéractives** : Le rendu s'anime étape par étape lors de la construction et de la résolution, avec un support avancé des couleurs dans le terminal, paramétrable depuis la configuration.
