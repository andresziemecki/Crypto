from json import dumps
from pandas import read_json
from secrets import api_key, api_secret
from cryptomarket.exchange.client import Client
from logging import basicConfig, INFO, error

cryptos = ('ETHARS', 'XLMARS', 'BTCARS', 'EOSARS')

# mainFunction should be executed every one mminute
def mainFunction():

    # I can't share you api keys and api secrets, anyway you can get your own on cryptomkt for free
    client = Client(api_key, api_secret) 
    
    # the next requests cryptocurrency prices to cryptomkt -> https://developers.cryptomkt.com/es/#ticker
    markets = client.get_ticker()

    # markets is a a kind of dict, if doesn't have 'data' as a key, it means an error has ocurred
    if 'data' in markets:
        # next will get only the cryptos that I'd like to save
        result = filter_cryptos(filter = cryptos, data=markets)

        jsonString = dumps(result) # see example_jsonString.json file
        
        df = read_json(jsonString)

        # append df to a csv file in cloud storage or append to a sql table

    else: 
        error("Crypto API didn't return market data")


def filter_cryptos(filter, data):
    """
    filter the interested cryptos
    """
    result = list()
    for i in data['data']:
        if i['market'] in filter:
            result.append(i)
    return result


if __name__=='__main__':
    basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level= INFO,
        datefmt='%Y-%m-%d %H:%M:%S')
    mainFunction()