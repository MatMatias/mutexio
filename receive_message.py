import globals


def receive_message(socket):
    message_data, message_address = socket.recvfrom(globals.MESSAGE_HEADER)

    untreated_message = message_data.decode(globals.MESSAGE_FORMAT)
    last_separator_position = untreated_message.rfind("|")
    treated_message = untreated_message[:last_separator_position]

    return (treated_message, message_address)
