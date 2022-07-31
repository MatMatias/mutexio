import globals


def tcp_receive_message(connection):
    message_length = connection.recv(globals.MESSAGE_HEADER).decode(
        globals.MESSAGE_FORMAT
    )
    if message_length:
        message_length = int(message_length)
        message = connection.recv(message_length).decode(globals.MESSAGE_FORMAT)

        return message

    return "[BAD MESSAGE]"
