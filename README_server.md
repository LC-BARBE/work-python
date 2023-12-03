# Fichier Python : Server.py

## Server:
```python
def __init__(self):
    self.trainer = Trainer()
    self.server = WebsocketServer(port=8080, host="0.0.0.0")
    self.server.set_fn_new_client(self.new_client)
    self.server.set_fn_message_received(self.message_received)
```

- Initialise un objet Trainer (contenant le modèle et le scaler)
- Configure le serveur WebSocket.

### Main
```python
if __name__ == "__main__":
    my_server = MyServer()
    my_server.run_forever()
```
- Démarre le server

### Connection du mobile au server WebSocket

```python
        ===>Done
```

### Message_received

```python
    def message_received(self, client, server, message):
        # Charger le message JSON
        try:
            data = json.loads(message)
        except json.JSONDecodeError as e:
            print("Erreur lors de la lecture du message JSON :", e)
            return

        # Prédiction
        features = np.array([[data['x'], data['y'], data['z']]])
        features_scaled = self.trainer.scaler.transform(features)
        prediction = self.trainer.model.predict(features_scaled)
        print("Prédiction : {}".format(prediction[0]))
````

- Cette méthode est appelée chaque fois que le serveur reçoit un message du mobile.
- Elle charge le message , extrait x, y, z
- Normalise les données à l'aide du scaler du modèle
- Réalisation d'une prédiction