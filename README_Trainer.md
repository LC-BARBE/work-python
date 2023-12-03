# Fichier Trainer

### Chargement des données

````python
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
````
- Cette partie nous permet de récuperer les données créer pendant la procédure LoadModelExpected.

### Extraiction des doonées x, y, z dans un tableau et un tableau de valeur attendue
````python
X = np.array([[entry['x'], entry['y'], entry['z']] for entry in data])
y = np.array(['haut'] * len(data_haut) + ['bas'] * len(data_bas) + ['gauche'] * len(data_gauche) + ['droite'] * len(data_droite))

````

### Division des données

````python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

````
- On divise les données en X_train, y_train et X_test, y_test. L'argument test_size=0.2 nous permet de spécifier que 20% des données seront utilisées pour les test et 80% pour le training. 
- Cela nous permet d'utiliser une partie des données pour régler nos poids et le biais. - - Et une autre partie des données pour vérifier que le predict renvoie la bonne valeur attendue une fois l'entrainement réalisé.

### Normalisation des données

````python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
````
- Le scaler nous permet de manier les données selon un écart type entre -1 et 1
- En d'autre terme elle harmonise les données afin qu'il soit toujours entre -1 et 1, même si x vari entre 900 et 1000 et y entre 10 et 40 les données traier pour régler les poids seront elle entre -1 et 1   

### Entraînement du modèle de réseau de neurones

````python
model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, random_state=42)
model.fit(X_train_scaled, y_train)
````

- On crée et entraîne un modèle de réseau de neurones avec une couche cachée de 100 neurones. Le methode fit() apporte des réglage au poids. 

````python
y_pred = model.predict(X_test_scaled)
````
- On récupère des prédictions sur le doonées test.

### Évaluation de la performance du modèle

````python
accuracy = accuracy_score(y_test, y_pred)
print("Pourcentage de validité : {:.2f}%".format(accuracy * 100))
````

Ces lignes calculent la précision du modèle en comparant les prédictions (y_pred) aux étiquettes réelles (y_test). La précision est ensuite affichée en pourcentage.

