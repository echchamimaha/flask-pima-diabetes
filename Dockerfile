# Image de base Python 3.10 slim
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du projet
COPY . .

# Exposer le port sur lequel Flask tournera
EXPOSE 5000

# Commande pour lancer l'application
CMD ["python", "app.py"]
