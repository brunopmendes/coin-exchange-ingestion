import requests

class CurrencyApi:

    def __init__(self, api_key):                
        self.__base_url = self.__get_base_url()
        self.__api_key = api_key

    def __get_base_url(self):
        return 'https://free.currconv.com/api/v7'

    def get_all_currencies(self):       
            r = requests.get(f'{self.__base_url}/currencies?apiKey={self.__api_key}')
            if r.status_code == 200 and r.headers['content-type'] == 'application/json; charset=utf-8':
                return r.json()
            else:
                raise Exception('api inválida, status diferente de 200')            

    def convert_real(self, coin_to_convert):
        r = requests.get(f'{self.__base_url}/convert?q=BRL_{coin_to_convert},{coin_to_convert}_BRL&compact=ultra&apiKey={self.__api_key}')
        if r.status_code == 200 and r.headers['content-type'] == 'application/json; charset=utf-8':
            return r.json()
        else:
            raise Exception('api inválida, status diferente de 200')