import sys

sys.path.append("..")

import globals
from send_message import send_message
from request_access import request_access

from socket import socket
from threading import Thread
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

    client = socket(globals.SOCKET_FAMILY, globals.SOCKET_PROTOCOL)

    request_loop_thread = Thread(target=request_access, args=(client, client_id))
    request_loop_thread.start()


init()
