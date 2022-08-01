import sys

sys.path.append("..")

import globals
from receive_message import receive_message
from log import log


def listen_requests(server_socket, client_requests, client_requests_lock, grant_event):
    print("[LISTENING] Server is listening requests.")

    while True:
        message, address = receive_message(server_socket)
        sender_request, sender_id = message.split("|")

        if sender_request == globals.REQUEST_COMMAND:
            client_requests_lock.acquire()
            client_requests.put((sender_id, sender_request, address))
            client_requests_lock.release()

        elif sender_request == globals.RELEASE_COMMAND:
            grant_event.clear()
            log(f"[ACCESS RELEASED] {sender_id}")

        else:
            log(f"[BAD REQUEST] from {sender_id}")

        log(f"[{sender_id} SENT] {sender_request}")
