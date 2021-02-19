import socket
import json
import logging
import api

logging.basicConfig(filename='logs.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s:')
logging.info("Server starts")


class WSServer:

    def __init__(self, host, port,):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(2)
        print("Server on")
        logging.info("Server on")

    def work_forever(self, buffer):

        while True:
            try:
                client_socket, address = self.server_socket.accept()
                logging.info('received connection from: ' + str(address))
                req_msg = json.loads(client_socket.recv(buffer).decode("utf8"))
                data_req_msg = req_msg['data']
                logging.info("Received message: " + str(req_msg))

                res_msg={}
                server_api = api.Api(data_req_msg['base_currency_code'])

                if res_msg['code'] == 'list_all_currencies_req':
                    res_msg['code'] = 'list_all_currencies_res'
                    res_msg['data'] = server_api.rates
                    logging.info("Sent list of currencies")

                elif res_msg['code'] == 'check_conversion_rate_req':
                    res_msg['code'] = 'check_conversion_rate_res'
                    if data_req_msg['filter'] == "null":
                        res_msg['data'] = server_api.rates
                    else:
                        res_msg['data'] = {"base_currency_code": data_req_msg['base_currency_code'],"rates": server_api.check_conversion_rate(data_req_msg['filter'])}

                elif res_msg['code'] == 'convert_currency_req':
                    res_msg['code'] = 'convert_currency_res'
                    res_msg['data'] = {"base_currency_code": data_req_msg['base_currency_code'],'Amount': data_req_msg['amount'],'Converted_to': data_req_msg['convert_to'],'Converted_amount': server_api.convert_currency(data_req_msg['amount'], data_req_msg['convert_to']),"Date":server_api.res_msg['date']}

                answer = str(str(res_msg).replace("\'", "\""))
                client_socket.send(str.encode(answer))  # .encode("utf8")

            except Exception as E:
                logging.critical("Excepction occured: " + str(E))
                client_socket.send(str.encode(str(E)))
                print (E)
                continue


server = WSServer('192.168.0.40', 33000)
server.work_forever(1024)
