"""
SDK: https://github.com/cryptomkt/cryptomkt-python
"""

from json import dumps
from time import sleep
from pandas import read_json
from config import logError

cryptos = ('ETHARS', 'XLMARS', 'BTCARS', 'EOSARS')

def filter_cryptos(filter, data):
    result = list()
    for i in data['data']:
        if i['market'] in filter:
            result.append(i)
    return result

def collect_data(client, conn):

    while(True):

        markets = client.get_ticker()

        if 'data' in markets:
            result = filter_cryptos(filter = cryptos, data=markets)
            jsonString = dumps(result) 
            df = read_json(jsonString)

            df.to_sql('tickers', con=conn, if_exists='append', index=False)
            sleep(30)

        else: 
            logError("Crypto API didn't return market data")
            sleep(5)
    # conn.close()