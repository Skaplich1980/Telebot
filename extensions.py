import json
import requests
from config import keys

class APIException(Exception):
    pass

class getAPI:
    @staticmethod
    def checkVariable(quote:str, base:str, amount:str):
        if quote==base:  # одинаковые валюты
            raise APIException(f'Нет смысла переводить одинаковые валюты {base}')

        # обработка неправильного ввода валюты
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {val}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        getAPI.checkVariable(quote, base, amount)
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        text = json.loads(r.content)[keys[base]]

        price = text * float(amount)
        price = round(price, 2)  # округление до копеек
        m = f"Цена {amount} {base} в {quote} : {price}"
        return m
