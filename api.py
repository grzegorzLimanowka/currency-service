import requests
import json
import config
import logging

logging.basicConfig(filename='logs.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s:')


class Api:

    def __init__(self, base_currency):
        self.base = base_currency
        logging.info("Downloading data from Api")
        while True:
            try:
                self.api = requests.get(config.address)
                self.address=requests.get(config.address)
                self.data = json.loads(self.address.text)
                self.rates = self.data['rates']
            except Exception as E:
                logging.critical("Cannot pull data from API: " + str(E))
                print(E)
                continue
            break

    def check_conversion_rate(self, filter):
        if isinstance(filter, str):
            answer = self.rates(filter)
        else:
            answer = {self.base: self.rates[self.base]}
            for x in range(len(filter)):
                answer[filter[x]] = self.rates[filter[x]]

        return answer

    def convert_currency(self, amount, towhat):
        return float(amount) / self.rates[self.base] * self.rates[towhat]

# a=Api("PLN")
# print(a.check_conversion_rate(["USD","EUR"]))
# print(a.check_conversion_rate("USD"))
