
import json
from websocket_server import WebsocketServer

def new_client(client, server):
    print("Nouveau client connecté : {}".format(client["address"]))

def message_received(client, server, message):
    global position, data_buffer

    # Charger le message JSON
    try:
        data = json.loads(message)
    except json.JSONDecodeError as e:
        print("Erreur lors de la lecture du message JSON :", e)
        return

    data_buffer.append(data)

    if len(data_buffer) == 100:
        filename = "{}.txt".format(position)
        with open(filename, 'a') as file:  
            for coord in data_buffer:
                file.write(f'{coord}\n')
        print("Les coordonnées ont été ajoutées à {}".format(filename))
        data_buffer = []
    
def start_server():
    global server
    server = WebsocketServer(port=8080, host="0.0.0.0")
    server.set_fn_new_client(new_client)
    server.set_fn_message_received(message_received)

    print("Serveur en attente de connexion...")
    server.run_forever()

def main():
    global position, data_buffer

    while True:
        position = input("Entrez la position du portable (h/haut, b/bas, g/gauche, d/droite) ou 'q' pour quitter : ").lower()

        if position == 'q':
            break  # Quitter la boucle
        data_buffer = []  

        start_server()

        server.server_close()

if __name__ == "__main__":
    main()