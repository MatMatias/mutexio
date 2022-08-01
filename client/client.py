import globals
from request_access import request_access
from listen_grant import listen_grant
from send_actions import send_actions

from socket import socket
from threading import Thread, Event


def init(client_id, request_limit):

    access_granted_event = Event()
    udp_client = socket(globals.SOCKET_FAMILY, globals.SOCKET_UDP)

    request_loop_thread = Thread(
        name=f"client {client_id} request access thread",
        target=request_access,
        args=(udp_client, client_id, access_granted_event, request_limit),
    )
    request_loop_thread.start()

    grant_listener_thread = Thread(
        name=f"client {client_id} grant listener thread",
        target=listen_grant,
        args=(udp_client, access_granted_event, request_limit, client_id),
    )
    grant_listener_thread.start()

    send_actions_thread = Thread(
        name=f"client {client_id} send actions thread",
        target=send_actions,
        args=(client_id, udp_client, access_granted_event, request_limit),
    )
    send_actions_thread.start()
