import globals


def receive_message(socket):
    message_header, header_address = socket.recvfrom(globals.MESSAGE_HEADER)

    message_header = message_header.decode(globals.MESSAGE_FORMAT)

    if message_header:
        message_length = int(message_header)

        message_data, message_address = socket.recvfrom(message_length)
        message_data = message_data.decode(globals.MESSAGE_FORMAT)

        global error_message
        error_message = (
            f"[BAD MESSAGE] Bad message from H:{header_address} M:{message_address}"
        )

        if message_data and message_address == header_address:
            return (message_data, message_address)

    return error_message
