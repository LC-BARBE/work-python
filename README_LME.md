## Load Model Expected

- Cette page de script nous permet de récupérer les 100 mesure relevées par l'accelerometre.
- Et stocke ces données dans un fichier .txt

----------
### Fonction principale
main():
global position, data_buffer

````
    while True:
        position = input("Entrez la position du portable (h/haut, b/bas, g/gauche, d/droite) ou 'q' pour quitter : ").lower()

        if position == 'q':
            break

        data_buffer = []  # Réinitialiser le tampon de données

        start_server()

        server.server_close()
````

- Un fois le fichier lancé. Le prompt demande quel position enregistrer haut, bas, etc...
- La réponse de l'utilisateur fournit le noml du fichier à créer.
- Il lance le server avec start_server et attends la connexion du mobile au server WebSocket.


### Fonction appelée lorsqu'un nouveau client se connecte
new_client(client, server):
````
def new_client(client, server):
    print("Nouveau client connecté : {}".format(client["address"]))
````
- Celle-ci nous permet de savoir que notre mobile est connecté.
- Une fois cela nous pouvons mettre le mobile dans la position nécessaire au relevé. 
- Et appuyé sur "send" en maintenant la position le temps d'enregistrer les résultats.
- Au moment de recevoir les mesures, celle-ci passe par la methode message_received

### Fonction appelée lorsqu'une mesure est reçu du mobile
message_received(client, server, message):
    global position, data_buffer
````
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
````
- Nous pouvons voir que la methode récupère le contenu du message et alimente le DataSet tant que celui-ci n'a pas atteint 100 iteration
- Enfin quand le compte est à son terme. Le dataset est inséré dans le fichier.

### Fonction pour démarrer le serveur WebSocket
def start_server():
    global server
    server = WebsocketServer(port=8080, host="0.0.0.0")
    server.set_fn_new_client(new_client)
    server.set_fn_message_received(message_received)

    print("Serveur en attente de connexion...")
    server.run_forever()