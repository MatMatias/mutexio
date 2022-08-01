import globals


def send_message(socket, message, address):
    message_ascii_length = len(message.encode(globals.MESSAGE_FORMAT))
    filler_string = "|"
    for _ in range(message_ascii_length - 1):
        filler_string += "0"

    message = message + filler_string
    message.encode()
    message = message.encode(globals.MESSAGE_FORMAT)

    socket.sendto(message, address)
