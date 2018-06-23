import socket
import sys
from random import randint

from network_communication import send_message, receive_message


def validate_input(prompt, possible_results):
    while True:
        command = input(prompt)
        if command not in possible_results:
            print("Invalid input. Please input again")
        else:
            return command


listening_port = 100
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = randint(0, 65535)
try:
    sock.bind(("localhost", port))
except socket.error:
    print("Error creating socket")
    sys.exit()
print("Client started on port " + str(port))
send_message("Please provide socket", ("localhost", listening_port), sock)
data = receive_message(sock)[0]
verification_port = int(data)
server_address = ("localhost", verification_port)
option = validate_input("1 for register. 2 for login: ", ["1", "2"])
send_message(option, server_address, sock)
while True:
    user_name = input("Input user name: ")
    password = input("Input password: ")
    send_message(user_name, server_address, sock)
    send_message(password, server_address, sock)
    respond = receive_message(sock)[0]
    print(respond)
    if respond == "Success":
        break

while True:
    command = input("Input your command: ")
    send_message(message=command, sock=sock, address=server_address)
    result = receive_message(sock)[0]
    print(result)
    if result == "Saved":
        break