sql_create_tickers_table = """ CREATE TABLE IF NOT EXISTS tickers (
                                        id integer PRIMARY KEY,
                                        timestamp text NOT NULL,
                                        market text NOT NULL,
                                        ask text NOT NULL,
                                        bid text NOT NULL,
                                        high text NOT NULL,
                                        low text NOT NULL,
                                        last_price text NOT NULL,
                                        volume text NOT NULL
                                    ); """