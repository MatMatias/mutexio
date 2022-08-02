
# MutexIO
This project is a basic implementation of a centralized mutual exclusion algorthim, where a coordinator process will coordinate accesses from the non-coordinator processes to the critical area.

## Architecture
The coordinator process has an UDP Socket that will be listening for requests commands from the non-coordinator and storing it on a Queue. It will coordinate that queue to manage the accesses on the critical area and send a grant command to the non-coordinator that is first on the queue, if there is no other non-coordinator with access to the critical area. Besides that, it also listen for commands. UDP socket was chosen because it makes it easier to listen and send commands to multiple other processes, since there is no need for handshake connections with each one.
The non coordinator process has an UDP socket as well, and sends request commmands multiple times to the coordinator. In parallel, it keeps listening to grant commands from the server. Once the server sends a grant command, the non coordinator process opens "resutlado.txt" file on append mode and writes the current time and it's id on it.

### Critical Area
On that project, the critical area access is the writing of the process id and the current time (including miliseconds) in a file called "resultado.txt"

### Running
```console
$ python server/server.py
```
then, run:
```console
$ python run_clients.py --n N --r R
```
where N represents the number of non-coordinator processes that will be created and run, and R represents the number of requests to the critical area each non-coordinator process will make to the coordinator.

## Folder structure
```
├── client
│   ├── client.py
│   ├── listen_grant.py
│   ├── request_access.py
│   └── send_actions.py
├── server
│   ├── listen_actions.py
│   ├── listen_requests.py
│   ├── log.py
│   ├── manage_requests.py
│   └── server.py
├── globals.py
├── README.md
├── receive_message.py
├── run_clients.py
├── send_message.py
```

### Root folder
-- globals.py
On that file is present all globals constans and variables.

-- receive_message.py
Message receiving protocol, to receive messages from other sockets

-- send_message.py
Message sending protocol, to send messages to other sockets

### Messaging protocol
Messages are encoded as ascii and have 1024 bytes each. If the message has less then 1024 bytes, the leftover bytes will be filled with 0's, after a single "|".

### client folder
-- client.py
Has a function called init() that creates and run the three non-coordinator core threads:
1) request sender thread: send [R] requisitions to the coordinator process;
2) grant listener thread: listen to grant commands from the coordinator process;
3) send actions thread: once the process got access to the critical area, it opens "resultado.txt" on append mode, and writes the current time and it's id on it, then close it.

### server folder
-- server.py
Has a function called init() that creates and run the two coordinator core threads:
1) listen requests thread: listen for requests from the non-coordinator processes;
2) manage requests thread: runs the centralized mutual exclusion algorithm to manage the access to the critical area;
3) main thread: runs the interface, where a menu with three options are presented, that being:
    - 1) Print current request queue;
    - 2) Print how many times each process was anwsered;
    - 3) Close execution.
