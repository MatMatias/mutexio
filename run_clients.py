import sys

sys.path.append("./client/")

from client import init
from argparse import ArgumentParser
from threading import Thread


def argument_parser():
    parser = ArgumentParser(
        description="Create and run [n] non-coordinator processess that will make requests to the coordinator process [r] times"
    )
    parser.add_argument(
        "--n", type=int, help="how many process will run", required=True
    )
    parser.add_argument(
        "--r", type=int, help="how many request each process will make", required=True
    )
    args = parser.parse_args()

    return args


args = argument_parser()
process_counter = args.n
process_request_limit = args.r

for i in range(process_counter):
    client_id = f"C{i}"
    client_thread = Thread(
        name=f"client {client_id} thread",
        target=init,
        args=(client_id, process_request_limit),
    )
    client_thread.start()
