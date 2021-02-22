import socket
import ast

class WSClient:

    def __init__(self, host, port):

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

    def send_message(self, buffer):

        message={}
        message['code'] = input('Code: ')

        if message['code'] == "check_conversion_rate_req":
            filter = input('Filter: ')
            filter = ast.literal_eval(filter)
            base_currency_code = input('base_currency_code: ')
            message['data'] = {"base_currency_code": base_currency_code, 'filter': filter}
        elif message['code'] == "convert_currency_req":
            base_currency_code = input('Currency: ')
            amount = input('Amount: ')
            convert_to = input('Convert to: ')
            message['data'] = {"base_currency_code": base_currency_code, "amount": amount, "convert_to": convert_to}
        else:
            message['data'] = input('Data: ')

        send = str(str(message).replace("\'", "\""))
        self.client_socket.send(str.encode(send))
        print(self.client_socket.recv(buffer).decode())


client = WSClient('192.168.0.40', 33000)
client.send_message(1024)
