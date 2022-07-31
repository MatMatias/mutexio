import sys

sys.path.append("..")

import globals
from tcp_send_message import tcp_send_message
from tcp_receive_message import tcp_receive_message
from socket import socket, SHUT_RDWR


def send_actions(client_id, access_granted_event):
    while True:
        access_granted_event.wait()

        tcp_client_socket = socket(globals.SOCKET_FAMILY, globals.SOCKET_TCP)
        tcp_client_socket.connect(globals.TCP_SERVER_ADDRESS)

        print(f"[CONNECTED] {client_id} connected to the TCP Server")

        while access_granted_event.is_set():
            server_menu = tcp_receive_message(tcp_client_socket)
            chosen_action = input(f"{server_menu}>> ")

            if chosen_action == "3":
                tcp_send_message(tcp_client_socket, globals.RELEASE_COMMAND)
                access_granted_event.clear()

                tcp_client_socket.shutdown(SHUT_RDWR)
                tcp_client_socket.close()
            else:
                tcp_send_message(tcp_client_socket, chosen_action)
