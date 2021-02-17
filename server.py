import socket
import json
import logging
#from api import sayhello
import api



logging.basicConfig(filename='logs.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s:')
logging.info("Server starts")

HOST = '192.168.0.40'
PORT = 33000
BUFFER = 1024



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(2)
print("Server on")

try:
    while True:
        client_socket, address = server_socket.accept()
        print(f"Received connection from {address}")
        logging.info('received connection from: ' + str(address))
        message = client_socket.recv(BUFFER).decode("utf8")
        data = json.loads(message)

        truedata=data['data']
       #nibyapi=api.Api("a")

        if data['code'] == 'list_all_currencies_req':
            api.sayhello()
            mojeapi = api.Api(23)
            print("tupowinnobycmojeapi:")
            print(mojeapi.Check("AUD"))
            data['data']=api.Api.rates
            #nibyapi.work()

        elif data['code'] == 'check_conversion_rate_req':
            mojeapi = api.Api(23)
            print("tupowinnobycmojeapi:")
            print(mojeapi.Check(truedata['currency']))
            #basecurrency=truedata['base_currency_code']

            data['code'] = 'check_conversion_rate_res'
            #data['data'] = {"base_currency_code": "false", "id":userid['id']}
        elif data['code'] == 'get_all_logged_in_clients':
            data['code'] = 'get_all_logged_in_clients_res'
            #data['data'] = {"client_list": clients}
        else:
            logging.critical("WRONG CODE")

        answer = str(str(data).replace("\'", "\""))
        client_socket.send(str.encode(answer))  # .encode("utf8")

except KeyboardInterrupt:
    logging.critical("Server has been interrupted")

