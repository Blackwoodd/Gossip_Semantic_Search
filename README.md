# Gossip_Semantic_Search

## C'est quoi un embedding ?

Un **embedding** est une représentation numérique d'un texte (ou d'autres types de données) sous forme de vecteurs dans un espace de dimension réduite. Ces vecteurs permettent de capturer le sens et les relations sémantiques entre les mots ou phrases, facilitant ainsi des tâches comme la recherche sémantique ou la classification de textes.

## Différence entre POST et GET

- **GET** : Utilisé pour récupérer des informations depuis un serveur. Les paramètres sont généralement inclus dans l'URL.
- **POST** : Utilisé pour envoyer des données au serveur (ex. formulaires, authentification). Contrairement à GET, les données sont envoyées dans le corps de la requête et ne sont pas visibles dans l'URL.

## Installation des dépendances

Pour exécuter ce projet, il est nécessaire d'installer les bibliothèques utilisées, notamment **Flask** et **Sentence-Transformers**. Voici comment les installer :

```sh
pip install Flask sentence-transformers scikit-learn feedparser

```sh
python app.py

```sh
python search_test.py