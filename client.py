import socket
import json
import random

HOST = '192.168.0.40'
PORT = 33000
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
    currency = input('Currency: ')
    filter = input('Filter: ')
    data['data'] = {"base_currency_code": currency, "filter": filter}
else:
    data['data'] = input('Data: ')

dataSEND = str(str(data).replace("\'", "\""))

client_socket.send(str.encode(dataSEND))
print( client_socket.recv(BUFFER).decode())