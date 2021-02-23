import unittest
import requests
import config
import random
import api

api_test = api.Api("PLN")


class first_test(unittest.TestCase):


    def test_speed(self):
        speedtest = api.Api("") #time overall would be the speed of downloading data from API

    def test_check_conversion_rate(self):
        self.assertEqual({'PLN': 1, 'USD': 0.269766, 'EUR': 0.222125}, api_test.check_conversion_rate(["USD","EUR"]))
        self.assertEqual({'PLN': 1, 'USD': 0.269766}, api_test.check_conversion_rate('USD'))

    def test_convert_currency(self):
        self.assertEqual(2.69766, api_test.convert_currency(10,"USD"))


unittest.main()