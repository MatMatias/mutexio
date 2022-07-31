import sys

sys.path.append("..")

from send_message import send_message

import globals
import logging
from datetime import datetime


def manage_requests(server_socket, client_requests, client_requests_lock, grant_event):
    while True:
        if client_requests.empty() == False:
            id, request_command, address = client_requests.get()

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            if request_command != globals.REQUEST_COMMAND:
                logging.error(
                    f"[{current_time} REQUEST QUEUE] Bad request command from {id} - {address}"
                )
                return

            client_requests_lock.acquire()
            send_message(server_socket, globals.GRANT_COMMAND, address)
            print(f"[{current_time} ACCESS GRANTED] Access granted to {id}")

            client_requests_lock.release()
            grant_event.set()
