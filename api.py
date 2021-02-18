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
            data = json.loads(api.text)
            rates = data['rates']
        except Exception as E:
            logging.critical("Cannot pull api")
            print("Cannot pull api")
            continue
        break

    def __init__(self, base):
        self.base = base

    def check_conversion_rate(self, filter):
        answer = {self.base: self.rates[self.base]}
        for x in range(len(filter)):
            answer[filter[x]] = self.rates[filter[x]]
        return answer

    def convert_currency(self, amount, towhat):
        return float(amount) / self.rates[self.base] * self.rates[towhat]


#test
A=Api("PLN") #test
print(A.convert_currency(100,"USD")) #test