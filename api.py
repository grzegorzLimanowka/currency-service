import requests
import json
import config

def sayhello():
    print("greetings from api")
class Api:
    print("Downloading data from Api")
    while True:
        try:
            api = requests.get(config.address)
        except Exception as E:
            continue
        break
    data = json.loads(api.text)
    rates = data['rates']
    print(rates)

    def __init__(self, base):
        self.base=base
    def work(self):
        print("działa")

    def Check(self, towhat):
        return str(self.base+self.rates[towhat])




