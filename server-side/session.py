from network_communication import receive_message, send_message
from data_processor import DataProcessor
import sys


class Session:
    def __init__(self, user, socket, user_address):
        self.socket = socket
        self.user = user
        self.user_address = user_address

    def run(self):
        while True:
            data = receive_message(self.socket)[0]
            result = DataProcessor.process_input(input_string=data, user=self.user)
            send_message(message=result, sock=self.socket, address=self.user_address)
            if result == "Saved":
                sys.exit()