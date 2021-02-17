import socket
import json
import random

HOST = '192.168.0.40'
PORT = 33001
BUFFER = 1024


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))

message = '''
{   

}
'''
data = json.loads(message)


data['code'] = input('Code: ')
if data['code'] == "check_conversion_rate_req":
    base_currency_code = input('base_currency_code: ')
    filter = input('Filter: ')
    data['data'] = {"base_currency_code": base_currency_code, "filter": filter}
elif data['code'] == "check_conversion_rate_req":
    base_currency_code = input('Currency: ')
    amount = input('Amount: ')
    convert_to = input('Convert to: ')
    data['data'] = {"base_currency_code": base_currency_code, "amount": amount, "convert_to": convert_to}
else:
    data['data'] = input('Data: ')

dataSEND = str(str(data).replace("\'", "\""))

client_socket.send(str.encode(dataSEND))
print( client_socket.recv(BUFFER).decode())