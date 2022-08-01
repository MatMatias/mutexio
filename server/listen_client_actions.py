import sys

sys.path.append("..")

from tcp_send_message import tcp_send_message
from tcp_receive_message import tcp_receive_message

import globals
import logging
from datetime import datetime
from socket import socket


def listen_actions(tcp_server_socket, grant_event):

    tcp_server_socket.listen()

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(
        f"[{current_time} LISTENING] TCP Server is listening on {globals.SERVER_IP}:{globals.TCP_SERVER_PORT}"
    )

    while True:
        grant_event.wait()
        client_connection, client_address = tcp_server_socket.accept()

        while grant_event.is_set():
            actions_menu = f"Access granted to {globals.chosen_client_id}.\nChoose your action (1, 2 or 3):\n1) Print current request;\n2) Print how many times each process was anwsered;\n3) Close execution.\n"
            tcp_send_message(client_connection, actions_menu)

            client_action = tcp_receive_message(client_connection)

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            print(
                f"[{current_time} TCP CLIENT {globals.chosen_client_id} SENT] {client_action}"
            )
            if client_action == globals.RELEASE_COMMAND:
                print(
                    f"[{current_time} TCP CLIENT {globals.chosen_client_id} CONNECTION CLOSED]"
                )
                grant_event.clear()
