import sys

sys.path.append("..")

from send_message import send_message

import globals
from datetime import datetime
from time import sleep


def send_actions(client_id, client_socket, access_granted_event):
    while True:
        access_granted_event.wait()

        with open("../resultado.txt", "a") as results:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S:%f")
            log = f"[{client_id}] {current_time}\n"
            results.write(log)

        message = f"{globals.RELEASE_COMMAND}|{client_id}"
        send_message(client_socket, message, globals.UDP_SERVER_ADDRESS)
        access_granted_event.clear()
