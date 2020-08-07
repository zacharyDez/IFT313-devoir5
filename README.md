# Implémentation de l'algorithme FIRST

**Zachary Déziel** (zachary.deziel@usherbrooke.ca)

**Samuel Hamman**

## Description

Implémentation de l'algorithm FIRST pour le devoir 5 (final) de IFT313. 

Une structure de donnée *Grammaire* est définie d'abord dans langage_formel/Grammaire
pour ensuite implémenter l'algorithme.

La définition du mot implémenter est assumé être la même
que celle établie après avoir eu la rétroaction au devoir 1. C'est-à-dire,
implémenter nécessite de construire toutes les primitives nécessaire pour le travail.

C'est pour cette raison qu'une structure de donnée *Grammaire* est définie d'abord dans langage_formel/Grammaire
pour ensuite implémenter l'algorithme FIRST.

Nous avons tout de même assumé que nous pouvons utilisé des primitives comme la structure de donnée file (*queue*)
 de la librairie standard de *Python*.
 
 ## Utilisation
 
Pour des exemples d'utilisation voir les tests dans le dossiers langage_formel/tests.

La seule dépendance, autre que *Python3*, est *pytest*.

Vous pouvez l'installer avec:

```bash
pip install pytest
```

Les tests peuvent être exécuté avec (mettre le flag `-v` pour plus de détails):

```bash
pytest
```

 