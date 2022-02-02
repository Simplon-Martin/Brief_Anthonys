# Brief project
Développer une application à partir d'une base de données de produits consommées au USA.

## Installation

Suivre les indications ci-dessous :

```bash
git clone https://github.com/Simplon-Martin/Brief_Anthonys.git
cd flaskProject/
```

Sous Windows : 

```bash
python -m venv venv
```

Sous Linux : 

```bash
source venv/bin/activate
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
cp exemple_config.yml instance/config.yml
```
Créer une BDD Mysql :
```sql
CREATE DATABASE  IF NOT EXISTS `flask_project` /*!40100 DEFAULT CHARACTER SET utf8mb4 */ /*!80016 DEFAULT ENCRYPTION='N' */;
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