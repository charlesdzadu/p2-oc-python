# Books To Scrape - Extracteur de données

Ce projet est un script Python conçu pour extraire (scraper) les informations des livres du site [Books to Scrape](https://books.toscrape.com/). Il permet de récupérer les données de tous les livres disponibles sur le site et de les sauvegarder dans un fichier CSV.

## 🚀 Fonctionnalités

- Extraction des données de tous les livres par catégorie
- Sauvegarde des informations dans un fichier CSV
- Suivi de la progression de l'extraction en temps réel
- Gestion des erreurs et des exceptions
- Support pour les URLs personnalisées

## 📋 Données extraites

Pour chaque livre, les informations suivantes sont extraites :
- URL de la page du produit
- Code produit universel (UPC)
- Titre du livre
- Prix TTC
- Prix HT
- Nombre d'exemplaires disponibles
- Description du produit
- Catégorie
- Note d'évaluation
- URL de l'image

## 💻 Prérequis

- Python 3.x
- pip (gestionnaire de paquets Python)

## ⚙️ Installation

1. Clonez ce dépôt :
```bash
git clone https://github.com/charlesdzadu/p2-oc-python.git
cd p2-oc-python
```

2. Créez un environnement virtuel et activez-le :
```bash
python -m venv .venv
source .venv/bin/activate  # Sur Unix/macOS
# ou
.venv\Scripts\activate  # Sur Windows
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## 🎯 Utilisation

### Exécution du script principal
Pour lancer le script principal qui extraira toutes les données du site :
```bash
python main.py
```
Les données seront automatiquement sauvegardées dans `assets/books_data.csv`

### Scripts additionnels
Le projet contient également d'autres scripts avec des fonctionnalités spécifiques :

- `scrape_book_website.py` : Pour extraire les données du site entier avec un chemin de sortie personnalisé
```bash
python scrape_book_website.py chemin/vers/mon_fichier.csv
```

- `scrape_single_category.py` : Pour extraire les données d'une catégorie spécifique
- `scrape_single_page.py` : Pour extraire les données d'une seule page de livre

## 📁 Structure du projet

- `main.py` : Point d'entrée principal du script (pas de paramètres personnalisables)
- `scrape_book_website.py` : Gestion de l'extraction des données du site entier
- `scrape_single_category.py` : Extraction des données d'une catégorie spécifique
- `scrape_single_page.py` : Extraction des données d'une page de livre
- `helpers.py` : Fonctions utilitaires
- `requirements.txt` : Liste des dépendances Python
- `assets/` : Dossier de stockage des données extraites

## 🛠️ Dépendances principales

- beautifulsoup4 : Pour l'analyse du HTML
- requests : Pour les requêtes HTTP

