import sys

sys.path.append("..")

import globals
from send_message import send_message

from time import sleep


def request_access(client_socket, client_id, access_granted_event):
    while True:
        while not access_granted_event.is_set():
            message = f"{globals.REQUEST_COMMAND}|{client_id}"
            send_message(client_socket, message, globals.UDP_SERVER_ADDRESS)
            print(f"[MESSAGE SENT] {message}")
            sleep(5)
