import sys

sys.path.append("..")

import globals
from request_access import request_access
from listen_grant import listen_grant
from send_actions import send_actions

from socket import socket
from threading import Thread, Event
from time import sleep
from argparse import ArgumentParser


def argument_parser():
    parser = ArgumentParser(description="creates a non-coordinator process")
    parser.add_argument("--id", type=str, help="process id.", required=True)
    args = parser.parse_args()

    return args


def init():
    args = argument_parser()
    client_id = args.id

    access_granted_event = Event()
    udp_client = socket(globals.SOCKET_FAMILY, globals.SOCKET_UDP)

    request_loop_thread = Thread(
        name="request access thread",
        target=request_access,
        args=(udp_client, client_id, access_granted_event),
    )
    request_loop_thread.start()

    grant_listener_thread = Thread(
        name="grant listener thread",
        target=listen_grant,
        args=(udp_client, access_granted_event),
    )
    grant_listener_thread.start()

    send_actions_thread = Thread(
        name="send actions thread",
        target=send_actions,
        args=(client_id, access_granted_event),
    )
    send_actions_thread.start()


init()
