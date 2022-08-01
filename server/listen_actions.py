import sys

sys.path.append("..")

import globals


def listen_actions(client_requests):
    while True:
        menu_message = f"Choose your action (1, 2 or 3):\n1) Print current request queue;\n2) Print how many times each process was anwsered;\n3) Close execution.\n"
        chosen_action = input(f"{menu_message}>> ")

        if chosen_action == "1":
            print("Current requests queue:\n")
            message = "(\n"
            for request in list(client_requests.queue):
                message += "    (" + request[0] + ", " + request[1] + "),\n"

            message += ")\n"
            print(message)

        if chosen_action == "2":
            if globals.chosen_client_id not in globals.process_answered_counters:
                print("No process was answered yet.")
            else:
                message = "(\n"
                for id in globals.process_answered_counters:
                    message += (
                        "    "
                        + id
                        + " process was answered "
                        + str(globals.process_answered_counters[id])
                        + " times,\n"
                    )
                message += ")\n"
                print(message)

        if chosen_action == "3":
            print("[SERVER TERMINATED]")
            break

    return
