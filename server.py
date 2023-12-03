from websocket_server import WebsocketServer
from Trainer import Trainer
import json
import numpy as np


class Server:

    def __init__(self):
        self.trainer = Trainer()
        self.InstServer = WebsocketServer(port=8080, host="0.0.0.0")
        self.InstServer.set_fn_new_client(self.new_client)
        self.InstServer.set_fn_message_received(self.message_received)

    def new_client(self, client, server):
        print("Nouveau client connecté : {}".format(client["address"]))

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

    def run_forever(self):
        self.server.run_forever()


if __name__ == "__main__":
    server = MyServer()
    server.run_forever()
