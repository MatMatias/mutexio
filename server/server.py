import sys

sys.path.append("..")

import globals
from receive_message import receive_message
from listen_requests import listen_requests
from manage_requests import manage_requests

from socket import socket
from queue import Queue
from threading import Event, Thread, Lock

client_requests = Queue()


def init():
    print("[STARTING] Server is starting...")

    server = socket(globals.SOCKET_FAMILY, globals.SOCKET_PROTOCOL)
    server.bind(globals.SERVER_ADDRESS)

    client_requests_lock = Lock()
    grant_event = Event()

    listen_requests_thread = Thread(
        name="requests listener thread",
        target=listen_requests,
        args=(server, client_requests, client_requests_lock),
    )
    listen_requests_thread.start()

    manage_requests_thread = Thread(
        name="requests manager thread",
        target=manage_requests,
        args=(server, client_requests, client_requests_lock, grant_event),
    )
    manage_requests_thread.start()


init()
