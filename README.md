# Semaine 1: Le jeu du serpent

Ce dépôt contient le code de démarrage pour le TP "le jeu du serpent" du
cours Python à Mines ParisTech.

Comme précisé durant le TP, nous recommandons d'installer les éléments
suivant sur votre ordinateur:

- [Anaconda]/[Miniconda] pour disposer d'un Python récent et des
    principales librairies utiles
- un étiteur de code, par défaut nous conseillons [Visual Studio Code]
- l'outil [git] avec ou sans interface graphique. En cas de soucis,
    l'interface [Github Desktop] permet de suivre facilement les besoins
    du cours.

## Code de démarrage

Le fichier `main.py` contient le code de démarrage du projet, tel que 
présenté sur les slides passés en cours.

## Setup

Un fois Anaconda installé, il faut créer un envisonnement dédié avec les
commandes suivantes:

```sh
$ conda create -n pas1 python=3.7
$ conda activate pas1
$ conda install pop
$ pip install pygame
```

## Exécution

On démarre le programme en invoquant l'interpréteur Python:

```sh
$ python starter.py
```

[Anaconda]: https://www.anaconda.com
[Miniconda]: https://docs.conda.io/en/latest/miniconda.html
[Visual Studio Code]: https://code.visualstudio.com
[git]: https://git-scm.com
[Github Desktop]: https://desktop.github.com

