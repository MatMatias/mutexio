from datetime import datetime


def log(message):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    with open("./server_log.txt", "a") as server_log:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S:%f")

        log = f"[{current_time}] {message}\n"
        server_log.write(log)
