import sys

sys.path.append("..")

import globals
from receive_message import receive_message
from listen_requests import listen_requests
from manage_requests import manage_requests
from listen_actions import listen_actions

from socket import socket
from queue import Queue
from threading import Event, Thread, Lock

client_requests = Queue()


def init():
    print("[STARTING] Udp Server is starting...")
    udp_server = socket(globals.SOCKET_FAMILY, globals.SOCKET_UDP)
    udp_server.bind(globals.UDP_SERVER_ADDRESS)

    print("[STARTING] Tcp Server is starting...")
    tcp_server = socket(globals.SOCKET_FAMILY, globals.SOCKET_TCP)
    tcp_server.bind(globals.TCP_SERVER_ADDRESS)

    client_requests_lock = Lock()
    chosen_client_id_lock = Lock()
    grant_event = Event()

    listen_requests_thread = Thread(
        name="requests listener thread",
        target=listen_requests,
        args=(udp_server, client_requests, client_requests_lock, grant_event),
        daemon=True,
    )
    listen_requests_thread.start()

    manage_requests_thread = Thread(
        name="requests manager thread",
        target=manage_requests,
        args=(
            udp_server,
            client_requests,
            client_requests_lock,
            grant_event,
            chosen_client_id_lock,
        ),
        daemon=True,
    )
    manage_requests_thread.start()

    listen_actions(client_requests)


init()
