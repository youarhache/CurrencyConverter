# CurrencyConverter

## Installer l'extension Pytest BDD à Visual Studio Code

Menu : Code/Preferences/Extensions
Chercher "pytest bdd" 

## Installer les dépendances
### En utilisant PYPI
```` pip install -r requirements.txt ````

### En utilisant Anaconda
```` conda create -n <mon_environnement> --file requirements.txt ````

## Pour générer le rapport specflow :

- lancer le rapport 
```` pytest --cucumberjson=<chemin/vers/mon/rapport/json> ````
