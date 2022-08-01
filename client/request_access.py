import sys

sys.path.append("..")

import globals
from send_message import send_message


def request_access(client_socket, client_id, access_granted_event, request_limit):
    request_counter = 0
    requesting = True

    while requesting:
        while not access_granted_event.is_set():
            message = f"{globals.REQUEST_COMMAND}|{client_id}"
            send_message(client_socket, message, globals.UDP_SERVER_ADDRESS)
            print(f"[MESSAGE SENT] {message}")

            request_counter += 1
            if request_counter >= request_limit:
                requesting = False
                break
