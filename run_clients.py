import sys

sys.path.append("./client/")

from client import init
from argparse import ArgumentParser
from threading import Thread


def argument_parser():
    parser = ArgumentParser(description="creates a non-coordinator process")
    parser.add_argument(
        "--n", type=int, help="how many process will run", required=True
    )
    args = parser.parse_args()

    return args


args = argument_parser()
process_counter = args.n

for i in range(process_counter):
    client_id = f"C{i}"
    client_thread = Thread(
        name=f"client {client_id} thread", target=init, args=(client_id,)
    )
    client_thread.start()
