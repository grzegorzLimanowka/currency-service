import socket
import json
import logging
#from api import sayhello
import api



logging.basicConfig(filename='logs.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s:')
logging.info("Server starts")

HOST = '192.168.0.40'
PORT = 33001
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
        server_api = api.Api(truedata['base_currency_code'])

        if data['code'] == 'list_all_currencies_req':
            data['data']=api.Api.rates
            logging.info("Sent list of currencies")
            #nibyapi.work()

        elif data['code'] == 'check_conversion_rate_req':

            print("tupowinnobycmojeapi:")
            print(server_api.Check(truedata['base_currency_code']))
            data['code'] = 'check_conversion_rate_res'
            data['data'] = {"rates": server_api.Check(truedata['filter'])}#, "id":userid['id']}

        elif data['code'] == 'convert_currency_req':
            data['code'] = 'convert_currency_res'
            data['data'] = {'Converted_amount': server_api.Convert(data['amount'],data['convert_to'])}

        else:
            logging.critical("WRONG CODE")

        answer = str(str(data).replace("\'", "\""))
        client_socket.send(str.encode(answer))  # .encode("utf8")

except KeyboardInterrupt:
    logging.critical("Server has been interrupted")

