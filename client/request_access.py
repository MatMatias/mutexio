import sys

sys.path.append("..")

import globals
from send_message import send_message

from time import sleep


def request_access(client_socket, client_id):
    connected = True

    while connected:
        message = f"{globals.REQUEST_COMMAND}|{client_id}"
        send_message(client_socket, message, globals.SERVER_ADDRESS)
        print(f"[MESSAGE SENT] {message}")
        sleep(5)
