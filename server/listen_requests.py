import sys

sys.path.append("..")

import globals
from receive_message import receive_message

import logging
from datetime import datetime


def listen_requests(server_socket, client_requests, client_requests_lock):
    print("[LISTENING] Server is listening requests.")

    while True:
        message, address = receive_message(server_socket)
        sender_request, sender_id = message.split("|")

        if sender_request == globals.REQUEST_COMMAND:
            client_requests_lock.acquire()

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            print(f"[{current_time} {sender_id} SENT] {sender_request}")
            client_requests.put((sender_id, sender_request, address))

            client_requests_lock.release()
        else:
            logging.error(f"[BAD REQUEST] from {sender_id}")
