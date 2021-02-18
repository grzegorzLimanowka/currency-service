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

        truedata = data['data']

        server_api = api.Api(truedata['base_currency_code'])

        if data['code'] == 'list_all_currencies_req':
            data['data'] = api.Api.rates
            logging.info("Sent list of currencies")

        elif data['code'] == 'check_conversion_rate_req':
            data['code'] = 'check_conversion_rate_res'
            if truedata['filter'] == "null":
                data['data'] = api.Api.rates
            else:
                data['data'] = {"base_currency_code": truedata['base_currency_code']}
                data['data'] = {"rates": server_api.check_conversion_rate(truedata['filter'])}

        elif data['code'] == 'convert_currency_req':
            data['code'] = 'convert_currency_res'
            data['data'] = {"base_currency_code": truedata['base_currency_code'],'Amount': truedata['amount'],'Converted_to': truedata['convert_to'],'Converted_amount': server_api.convert_currency(truedata['amount'], truedata['convert_to']),"Date":api.Api.data['date']}

        else:
            logging.critical("WRONG CODE")

        answer = str(str(data).replace("\'", "\""))
        client_socket.send(str.encode(answer))  # .encode("utf8")

except KeyboardInterrupt:
    logging.critical("Server has been interrupted")

