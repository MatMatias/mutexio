import sys

sys.path.append("..")

import globals
from receive_message import receive_message
from listen_requests import listen_requests

from socket import socket
from queue import Queue
from threading import Thread, Lock

client_requests = Queue()


def init():
    print("[STARTING] Server is starting...")

    server = socket(globals.SOCKET_FAMILY, globals.SOCKET_PROTOCOL)
    server.bind(globals.SERVER_ADDRESS)

    client_requests_lock = Lock()
    listen_requests_thread = Thread(
        name="requests listener thread",
        target=listen_requests,
        args=(server, client_requests, client_requests_lock),
    )
    listen_requests_thread.start()


init()
