Discord IP & Weather Bot
Description

Ce bot Discord permet d'extraire et d'afficher des informations sur les adresses IP mentionnées dans les messages du serveur. Il utilise l'API de ip-api.com pour obtenir les informations de localisation et l'API openweathermap.org pour récupérer les données météorologiques associées.
Fonctionnalités

    Détecte les adresses IP dans les messages Discord

    Récupère les informations de localisation (pays, région, ville, coordonnées, fournisseur d'accès Internet)

    Affiche la météo actuelle de l'emplacement détecté

    Fournit les résultats sous forme d'embed Discord stylisé

Prérequis

Avant d'exécuter ce bot, assurez-vous d'avoir installé :

    Python 3.8+

    Les bibliothèques suivantes (installables via pip):
    pip install discord requests

    Une clé API pour OpenWeatherMap (https://openweathermap.org/)

    Un token pour un bot Discord (obtenable depuis https://discord.com/developers/applications)

Installation et Configuration

    Clonez ce projet ou copiez le script sur votre machine.

    Remplacez les valeurs suivantes dans le script par vos propres clés :
    weather_api_key = "Your.api"
    discord_api_key = "Your.token"

    Exécutez le script avec la commande :
    python bot.py

Permissions et Sécurité

    Assurez-vous que votre bot dispose des permissions suffisantes pour lire et envoyer des messages dans le serveur Discord.

    Ne partagez pas vos clés API publiquement.

    Il est recommandé d'utiliser des variables d'environnement pour stocker les clés API au lieu de les inclure en dur dans le code.

Avertissements

    Ce bot n'effectue pas de requêtes pour vérifier la validité légale des adresses IP récupérées.

    Assurez-vous d'utiliser ce bot en accord avec les conditions d'utilisation des APIs utilisées et la réglementation de Discord.

Auteur

Développé par [lost/woly].
Licence

MIT License


