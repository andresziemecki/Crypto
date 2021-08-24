"""
SDK: https://github.com/cryptomkt/cryptomkt-python
"""

from json import dumps
from pandas import read_json
from config import logError

cryptos = ('ETHARS', 'XLMARS', 'BTCARS', 'EOSARS')



def collect_data(client, conn):

    markets = client.get_ticker()

    if 'data' in markets:
        result = filter_cryptos(filter = cryptos, data=markets)
        jsonString = dumps(result) 
        df = read_json(jsonString)

        df.to_sql('tickers', con=conn, if_exists='append', index=False)

    else: 
        logError("Crypto API didn't return market data")
    conn.close()