import sys

sys.path.append("..")

from send_message import send_message

import globals
import logging
from datetime import datetime


def manage_requests(
    server_socket,
    client_requests,
    client_requests_lock,
    grant_event,
    chosen_client_id_lock,
):
    while True:
        if not client_requests.empty() and not grant_event.is_set():
            client_requests_lock.acquire()
            chosen_client_id_lock.acquire()

            id, request_command, address = client_requests.get()
            globals.chosen_client_id = id

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            if request_command != globals.REQUEST_COMMAND:
                logging.error(
                    f"[{current_time} REQUEST QUEUE] Bad request command from {id} - {address}"
                )
                return

            send_message(server_socket, globals.GRANT_COMMAND, address)
            print(f"[{current_time} ACCESS GRANTED] Access granted to {id}")
            globals.process_answered_counters[id] += 1

            chosen_client_id_lock.release()
            client_requests_lock.release()
            grant_event.set()
