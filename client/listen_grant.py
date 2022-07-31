import sys

sys.path.append("..")

import globals
from receive_message import receive_message
from datetime import datetime
from time import sleep


def listen_grant(udp_client_socket, access_granted_event):
    while True:
        while not access_granted_event.is_set():
            server_message = receive_message(udp_client_socket)
            server_command = server_message[0]

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            print(f"[{current_time} SERVER SENT] {server_command}")

            if server_command == globals.GRANT_COMMAND:
                sleep(1)
                access_granted_event.set()
