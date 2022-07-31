import sys

sys.path.append("..")

import globals


def listen_actions(client_requests):
    while True:
        menu_message = f"Choose your action (1, 2 or 3):\n1) Print current request;\n2) Print how many times each process was anwsered;\n3) Close execution.\n"
        chosen_action = input(menu_message)

        if chosen_action == "1":
            print("Current requests queue:\n")
            message = "(\n"
            for request in client_requests:
                message += "(" + request[0] + ", " + request[1] + "),\n"

            print(message)

        if chosen_action == "2":
            if globals.chosen_client_id not in globals.process_answered_counters:
                print("No process was answered yet.")
            else:
                print(
                    f"Process {globals.chosen_client_id} was answered {globals.process_answered_counters[globals.chosen_client_id]}\n"
                )

        if chosen_action == "3":
            print("[SERVER TERMINATED]")
            break

    return
