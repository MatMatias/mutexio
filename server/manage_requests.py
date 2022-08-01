import sys

sys.path.append("..")

from send_message import send_message
from log import log

import globals


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

            if request_command != globals.REQUEST_COMMAND:
                log(f"[SERVER REQUEST QUEUE] Bad request command from {id} - {address}")
                return

            send_message(server_socket, globals.GRANT_COMMAND, address)
            log(f"[ACCESS GRANTED] {id}")

            if id not in globals.process_answered_counters:
                globals.process_answered_counters[id] = 0

            globals.process_answered_counters[id] += 1

            chosen_client_id_lock.release()
            client_requests_lock.release()
            grant_event.set()
