# Chatbot avec Interface Graphique en Python

Ce projet est un chatbot simple implémenté en Python avec une interface graphique construite à l'aide de **Tkinter**. Le chatbot peut répondre à des questions prédéfinies et utilise le modèle **TF-IDF** pour reconnaître des questions similaires. L'interface utilisateur inclut un **menu déroulant** pour sélectionner des questions, une zone de texte pour saisir des messages, et un affichage des réponses sous forme de bulles.

## Table des Matières
1. [Introduction](#introduction)
2. [Prérequis](#prérequis)
3. [Installation](#installation)
4. [Structure du projet](#structure-du-projet)
5. [Fonctionnalités](#fonctionnalités)
6. [Explication du code](#explication-du-code)
7. [Améliorations futures](#améliorations-futures)

## Introduction

Le projet consiste en un chatbot capable de répondre à des questions via une interface utilisateur agréable. Les questions sont reconnues grâce à un dictionnaire de correspondances exactes ou par correspondance approximative grâce au **modèle TF-IDF**. Le chatbot peut également afficher une liste de questions préexistantes via un menu déroulant, permettant à l'utilisateur de choisir rapidement une question.

## Prérequis

Avant de commencer, assurez-vous que votre machine dispose des éléments suivants :

- Python 3.x
- Bibliothèques Python suivantes :
  - `tkinter` (installé par défaut avec Python)
  - `scikit-learn` pour TF-IDF
  - `numpy` pour les opérations sur les matrices
  - `tkinter.scrolledtext` pour la zone de texte avec défilement

## Installation

1. Clonez le dépôt sur votre machine locale :
   ```bash
   git clone https://github.com/votre-repo/chatbot.git
   ```

2. Accédez au répertoire du projet :
   ```bash
   cd chatbot
   ```

3. Installez les dépendances nécessaires :
   ```bash
   pip install -r requirements.txt
   ```

## Structure du projet

Le projet est structuré de la manière suivante :

- `chatbot.py` : Le fichier principal contenant la logique du chatbot et l'interface graphique.
- `conversation.txt` : Un fichier texte contenant les questions et réponses du chatbot.
- `requirements.txt` : Un fichier texte contenant les dépendances du projet.

## Fonctionnalités

- **Questions et Réponses Prédéfinies** : Le chatbot peut répondre à des questions prédéfinies.
- **Menu Déroulant** : Permet à l'utilisateur de sélectionner une question parmi une liste préexistante.
- **Zone de Texte** : Utilisateur peut saisir des messages et envoyer.
- **Réponses Afficher** : Réponses du chatbot affichées dans une zone de texte avec défilement.

## Explication du code

Le code est structuré en plusieurs fonctions :

1. **send_message()** : Cette fonction est appelée lorsque l'utilisateur clique sur le bouton "Envoyer". Elle récupère le message saisi par l'utilisateur, le traite, et affiche la réponse du chatbot dans la zone de texte.

2. **get_response(user_input)** : Cette fonction prend en entrée le message de l'utilisateur, le traite, et retourne la réponse du chatbot. Elle utilise le modèle TF-IDF pour trouver la réponse la plus appropriée dans le dictionnaire des questions et réponses prédéfinies.

3. **load_conversation()** : Cette fonction charge les questions et réponses du fichier `conversation.txt` et les stocke dans des listes pour une utilisation ultérieure.

## Améliorations futures

1.	Amélioration des réponses TF-IDF : Utiliser des techniques NLP plus avancées pour améliorer la correspondance entre questions.
2.	Personnalisation des messages : Permettre à l’utilisateur d’ajouter des questions et réponses dynamiquement.
3.	Sauvegarde des conversations : Ajouter la possibilité de sauvegarder l’historique de la conversation.
4.	Intégration avec une API : Intégrer une API pour obtenir des informations en temps réel (par ex. météo, actualités).
5.	Amélioration de l’interface utilisateur : Ajouter des fonctionnalités graphiques pour rendre l’interface plus intuitive et agréable.

## Conclusion

Ce chatbot offre une expérience utilisateur agréable avec une interface intuitive et des réponses prédéfinies. Les fonctionnalités actuelles peuvent être étendues pour ajouter plus de dynamisme et de complexité, comme l’intégration avec une API ou un modèle d’IA plus avancé.

- Mathieu Soussignan.

