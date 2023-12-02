from websocket_server import WebsocketServer
from LoadModelExpected import LoadModelExpected

def new_client(client, server):
    print("Nouveau client connecté : {}".format(client["address"]))


def message_received(client, server, message):
    print(message)

server = WebsocketServer(port=8080, host="0.0.0.0")
server.set_fn_new_client(new_client)
server.set_fn_message_received(message_received)
server.run_forever()
