from config import setConfig
from secrets import api_key, api_secret
from collectors.cryptomkt import collect_data
from cryptomarket.exchange.client import Client

def main():

    print("Starting Bot...")

    conn = setConfig()

    client = Client(api_key, api_secret)
    
    collect_data(client, conn)


if __name__=='__main__':
    main()

    
    
