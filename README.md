# Brief project
Développer une application à partir d'une base de données de produits consommés au USA.

## Installation

Suivre les indications ci-dessous :

```bash
git clone https://github.com/Simplon-Martin/Brief_Anthonys.git
cd Brief_Anthonys/flaskProject/
```

Ensuite : 

```bash
pip install -r requirements.txt
```

## Configuration

Configuration
Ouvrir le fichier exemple_config.yml et remplacer les valeurs par défaut par celle de votre environnement. Copier ensuite ce fichier dans un dossier instance et le renommer config.yml.

```bash
mkdir instance
cp configsample.yml instance/config.yml
```
Créer une BDD Mysql :
```sql
CREATE DATABASE  IF NOT EXISTS `flask_project` /*!40100 DEFAULT CHARACTER SET utf8mb4 */ /*!80016 DEFAULT ENCRYPTION='N' */;
```

Si la commande 'flask' n'est pas reconnue, utilisez:
```bash
~/.local/bin/flask 
```

Générer le dossier "migrations" :
```bash
flask db init
```
Au besoin : 
```bash
flask db migrate
```
Création du script.sql et insertion des données : 
```bash
flask db upgrade
flask insert-db
```

Exécution
Pour lancer l'app, vous devrez taper la commande :

```bash
FLASK_ENV=development flask run --port 8080
```


## Contribution
Martin

## License
