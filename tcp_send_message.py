import globals


def tcp_send_message(tcp_socket, message):
    message = message.encode(globals.MESSAGE_FORMAT)
    message_length = len(message)

    send_length = str(message_length).encode(globals.MESSAGE_FORMAT)
    send_length += b" " * ((globals.MESSAGE_HEADER) - len(send_length))

    tcp_socket.send(send_length)
    tcp_socket.send(message)
