import requests
import json
import config
import logging

logging.basicConfig(filename='logs.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s:')



class Api:
    print("Downloading data from Api")
    while True:
        try:
            api = requests.get(config.address)
        except Exception as E:
            logging.critical("Cannot pull api")
            continue
        break
    data = json.loads(api.text)
    rates = data['rates']
    print(rates)

    def __init__(self, base):
        self.base=base
    def Check(self, base):

        print("base")

    def Convert(self, amount, towhat):
        return amount/self.rates[self.base]*self.rates[towhat]


    def sayhello():
        print("greetings from api")




