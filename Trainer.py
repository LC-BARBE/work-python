import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler


class Trainer:

    
    def __init__(self) -> None:
        pass

    # Charger les données
    def load_data(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            # convertir en dict
            data = [eval(line.strip()) for line in lines]  
        return data

    data_haut = load_data('positionFile/h.txt')
    data_bas = load_data('positionFile/b.txt')
    data_gauche = load_data('positionFile/g.txt')
    data_droite = load_data('positionFile/d.txt')

    data = data_haut + data_bas + data_gauche + data_droite

    # Extraire les caractéristiques (x, y, z) et les étiquettes
    X = np.array([[entry['x'], entry['y'], entry['z']] for entry in data])
    y = np.array(['haut'] * len(data_haut) + ['bas'] * len(data_bas) + ['gauche'] * len(data_gauche) + ['droite'] * len(data_droite))

    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Normaliser les données
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Créer et entraîner le modèle de réseau de neurones
    model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, random_state=42)
    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)

    # Calculer la précision du modèle
    accuracy = accuracy_score(y_test, y_pred)
    print("Précision du modèle : {:.2f}%".format(accuracy * 100))