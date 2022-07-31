import globals


def send_message(socket, message, address):
    message = message.encode(globals.MESSAGE_FORMAT)

    message_length = len(message)
    send_length = str(message_length).encode(globals.MESSAGE_FORMAT)
    send_length += b" " * ((globals.MESSAGE_HEADER) - len(send_length))

    socket.sendto(send_length, address)
    socket.sendto(message, address)
