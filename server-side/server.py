import socket
from random import randint
from threading import Thread

if __name__ == '__main__':
    from user import User
    from session import Session
else:
    from .user import User
    from .session import Session
from network_communication import send_message, receive_message
listening_port = 100


def handle_client_verification(private_socket, client_address):
    option = receive_message(private_socket)[0]
    user = None
    if option == '1':
        while True:
            user_name = receive_message(private_socket)[0]
            password = receive_message(private_socket)[0]
            if User.is_user_name_exist(user_name) or user_name == "":
                send_message("Choose another user name. Already exists or blank.", client_address, private_socket)
            else:
                User.add_user(user_name, password)
                send_message("Success", client_address, private_socket)
                print(user_name + " registered and login successfully")
                user = User(user_name)
                break
    elif option == '2':
        while True:
            user_name = receive_message(private_socket)[0]
            password = receive_message(private_socket)[0]
            if User.is_login_correct(user_name, password):
                send_message("Success", client_address, private_socket)
                print(user_name + " login successfully")
                user = User(user_name)
                break
            else:
                send_message("Incorrect", client_address, private_socket)
    session = Session(socket=private_socket, user=user, user_address= client_address)
    thread = Thread(target=session.run, args=())
    thread.start()
    thread.join()


listening_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
listening_sock.bind(("localhost", listening_port))
print("Server started on port 100")
while True:
    data, address = receive_message(listening_sock)
    print(str(address) + ":" + data)
    new_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    new_port = 0
    while True:
        new_port = randint(0, 65535)
        try:
            new_sock.bind(("localhost", new_port))
            break
        except socket.error:
            pass
    send_message(str(new_port), address, listening_sock)
    new_thread = Thread(target=handle_client_verification, args=(new_sock, address))
    new_thread.start()
