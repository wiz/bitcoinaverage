import requests
from decimal import Decimal

from bitcoinaverage.config import CURRENCY_LIST, DEC_PLACES
from bitcoinaverage.exceptions import NoVolumeException


def mtgoxApiCall(usd_api_url, eur_api_url, gbp_api_url, cad_api_url, rur_api_url, *args, **kwargs):
    usd_result = requests.get(usd_api_url).json()
    eur_result = requests.get(eur_api_url).json()
    gbp_result = requests.get(gbp_api_url).json()
    cad_result = requests.get(cad_api_url).json()
    rur_result = requests.get(rur_api_url).json()

    return {CURRENCY_LIST['USD']: {'ask': Decimal(usd_result['data']['sell']['value']).quantize(DEC_PLACES),
                                   'bid': Decimal(usd_result['data']['buy']['value']).quantize(DEC_PLACES),
                                   'high': Decimal(usd_result['data']['high']['value']).quantize(DEC_PLACES),
                                   'low': Decimal(usd_result['data']['low']['value']).quantize(DEC_PLACES),
                                   'last': Decimal(usd_result['data']['last']['value']).quantize(DEC_PLACES),
                                   'volume': Decimal(usd_result['data']['vol']['value']).quantize(DEC_PLACES),
    },
            CURRENCY_LIST['EUR']: {'ask': Decimal(eur_result['data']['sell']['value']).quantize(DEC_PLACES),
                                   'bid': Decimal(eur_result['data']['buy']['value']).quantize(DEC_PLACES),
                                   'high': Decimal(eur_result['data']['high']['value']).quantize(DEC_PLACES),
                                   'low': Decimal(eur_result['data']['low']['value']).quantize(DEC_PLACES),
                                   'last': Decimal(eur_result['data']['last']['value']).quantize(DEC_PLACES),
                                   'volume': Decimal(eur_result['data']['vol']['value']).quantize(DEC_PLACES),
            },
            CURRENCY_LIST['GBP']: {'ask': Decimal(gbp_result['data']['sell']['value']).quantize(DEC_PLACES),
                                   'bid': Decimal(gbp_result['data']['buy']['value']).quantize(DEC_PLACES),
                                   'high': Decimal(gbp_result['data']['high']['value']).quantize(DEC_PLACES),
                                   'low': Decimal(gbp_result['data']['low']['value']).quantize(DEC_PLACES),
                                   'last': Decimal(gbp_result['data']['last']['value']).quantize(DEC_PLACES),
                                   'volume': Decimal(gbp_result['data']['vol']['value']).quantize(DEC_PLACES),
            },
            CURRENCY_LIST['CAD']: {'ask': Decimal(cad_result['data']['sell']['value']).quantize(DEC_PLACES),
                                   'bid': Decimal(cad_result['data']['buy']['value']).quantize(DEC_PLACES),
                                   'high': Decimal(cad_result['data']['high']['value']).quantize(DEC_PLACES),
                                   'low': Decimal(cad_result['data']['low']['value']).quantize(DEC_PLACES),
                                   'last': Decimal(cad_result['data']['last']['value']).quantize(DEC_PLACES),
                                   'volume': Decimal(cad_result['data']['vol']['value']).quantize(DEC_PLACES),
            },
            CURRENCY_LIST['RUB']: {'ask': Decimal(rur_result['data']['sell']['value']).quantize(DEC_PLACES),
                                   'bid': Decimal(rur_result['data']['buy']['value']).quantize(DEC_PLACES),
                                   'high': Decimal(rur_result['data']['high']['value']).quantize(DEC_PLACES),
                                   'low': Decimal(rur_result['data']['low']['value']).quantize(DEC_PLACES),
                                   'last': Decimal(rur_result['data']['last']['value']).quantize(DEC_PLACES),
                                   'volume': Decimal(rur_result['data']['vol']['value']).quantize(DEC_PLACES),
            },
    }


def bitstampApiCall(api_url, *args, **kwargs):
    result = requests.get(api_url).json()

    return {CURRENCY_LIST['USD']: {'ask': Decimal(result['ask']).quantize(DEC_PLACES),
                                   'bid': Decimal(result['bid']).quantize(DEC_PLACES),
                                   'high': Decimal(result['high']).quantize(DEC_PLACES),
                                   'low': Decimal(result['low']).quantize(DEC_PLACES),
                                   'last': Decimal(result['last']).quantize(DEC_PLACES),
                                   'volume': Decimal(result['volume']).quantize(DEC_PLACES),
    }}


def campbxApiCall(api_url, *args, **kwargs):
    result = requests.get(api_url).json()

    #no volume provided
    # return_data = {CURRENCY_LIST['USD']: {'ask': Decimal(result['Best Ask']).quantize(DEC_PLACES),
    #                                'bid': Decimal(result['Best Bid']).quantize(DEC_PLACES),
    #                                'last': Decimal(result['Last Trade']).quantize(DEC_PLACES),
    #                                }}

    raise NoVolumeException


def btceApiCall(usd_api_url, eur_api_url, rur_api_url, *args, **kwargs):
    usd_result = requests.get(usd_api_url).json()
    eur_result = requests.get(eur_api_url).json()
    rur_result = requests.get(rur_api_url).json()

    #dirty hack, BTC-e has a bug in their APIs - buy/sell prices mixed up
    if usd_result['ticker']['sell'] < usd_result['ticker']['buy']:
        temp = usd_result['ticker']['buy']
        usd_result['ticker']['buy'] = usd_result['ticker']['sell']
        usd_result['ticker']['sell'] = temp

    if eur_result['ticker']['sell'] < eur_result['ticker']['buy']:
        temp = eur_result['ticker']['buy']
        eur_result['ticker']['buy'] = eur_result['ticker']['sell']
        eur_result['ticker']['sell'] = temp

    if rur_result['ticker']['sell'] < rur_result['ticker']['buy']:
        temp = rur_result['ticker']['buy']
        rur_result['ticker']['buy'] = rur_result['ticker']['sell']
        rur_result['ticker']['sell'] = temp

    return {CURRENCY_LIST['USD']: {'ask': Decimal(usd_result['ticker']['sell']).quantize(DEC_PLACES),
                                   'bid': Decimal(usd_result['ticker']['buy']).quantize(DEC_PLACES),
                                   'high': Decimal(usd_result['ticker']['high']).quantize(DEC_PLACES),
                                   'low': Decimal(usd_result['ticker']['low']).quantize(DEC_PLACES),
                                   'last': Decimal(usd_result['ticker']['last']).quantize(DEC_PLACES),
                                   'avg': Decimal(usd_result['ticker']['avg']).quantize(DEC_PLACES),
                                   'volume': Decimal(usd_result['ticker']['vol_cur']).quantize(DEC_PLACES),
    },
            CURRENCY_LIST['EUR']: {'ask': Decimal(eur_result['ticker']['sell']).quantize(DEC_PLACES),
                                   'bid': Decimal(eur_result['ticker']['buy']).quantize(DEC_PLACES),
                                   'high': Decimal(eur_result['ticker']['high']).quantize(DEC_PLACES),
                                   'low': Decimal(eur_result['ticker']['low']).quantize(DEC_PLACES),
                                   'last': Decimal(eur_result['ticker']['last']).quantize(DEC_PLACES),
                                   'avg': Decimal(eur_result['ticker']['avg']).quantize(DEC_PLACES),
                                   'volume': Decimal(eur_result['ticker']['vol_cur']).quantize(DEC_PLACES),
            },
            CURRENCY_LIST['RUB']: {'ask': Decimal(rur_result['ticker']['sell']).quantize(DEC_PLACES),
                                   'bid': Decimal(rur_result['ticker']['buy']).quantize(DEC_PLACES),
                                   'high': Decimal(rur_result['ticker']['high']).quantize(DEC_PLACES),
                                   'low': Decimal(rur_result['ticker']['low']).quantize(DEC_PLACES),
                                   'last': Decimal(rur_result['ticker']['last']).quantize(DEC_PLACES),
                                   'avg': Decimal(rur_result['ticker']['avg']).quantize(DEC_PLACES),
                                   'volume': Decimal(rur_result['ticker']['vol_cur']).quantize(DEC_PLACES),
            }}


def bitcurexApiCall(eur_api_url, *args, **kwargs):
    result = requests.get(eur_api_url).json()

    return {CURRENCY_LIST['EUR']: {'ask': Decimal(result['sell']).quantize(DEC_PLACES),
                                   'bid': Decimal(result['buy']).quantize(DEC_PLACES),
                                   'high': Decimal(result['high']).quantize(DEC_PLACES),
                                   'low': Decimal(result['low']).quantize(DEC_PLACES),
                                   'last': Decimal(result['last']).quantize(DEC_PLACES),
                                   'avg': Decimal(result['avg']).quantize(DEC_PLACES),
                                   'volume': Decimal(result['vol']).quantize(DEC_PLACES),
    }}


def vircurexApiCall(usd_api_url, eur_api_url, *args, **kwargs):
    usd_result = requests.get(usd_api_url).json()
    eur_result = requests.get(eur_api_url).json()

    return {CURRENCY_LIST['USD']: {'ask': Decimal(usd_result['lowest_ask']).quantize(DEC_PLACES),
                                   'bid': Decimal(usd_result['highest_bid']).quantize(DEC_PLACES),
                                   'last': Decimal(usd_result['last_trade']).quantize(DEC_PLACES),
                                   'volume': Decimal(usd_result['volume']).quantize(DEC_PLACES),
    },
            CURRENCY_LIST['EUR']: {'ask': Decimal(eur_result['lowest_ask']).quantize(DEC_PLACES),
                                   'bid': Decimal(eur_result['highest_bid']).quantize(DEC_PLACES),
                                   'last': Decimal(eur_result['last_trade']).quantize(DEC_PLACES),
                                   'volume': Decimal(eur_result['volume']).quantize(DEC_PLACES),
            },
    }

def bitbargainApiCall(gbp_api_url, *args, **kwargs):
    gbp_result = requests.get(gbp_api_url).json()


    average_btc = Decimal(gbp_result['response']['avg_24h'])
    volume_btc = (Decimal(gbp_result['response']['vol_24h']) / average_btc).quantize(DEC_PLACES)

    return {CURRENCY_LIST['GBP']: {'ask': average_btc.quantize(DEC_PLACES), #bitbargain is an OTC, so ask == last
                                   'bid': None, #bitbargain is an OTC, so no bids available
                                   'last': average_btc.quantize(DEC_PLACES),
                                   'volume': volume_btc,
                                    },
                }



#
#
# {"success": true, "response": {"high_24h": "78.0000000000",
#                                "low_24h": "63.3500000000",
#                                "avg_24h": "67.56309485765414",
#                                "vol_24h": "44884.1300000000",

#                                "high_7d": "78.0000000000",
#                                "low_7d": "60.0000000000",
#                                "avg_7d": "65.55231531056009",
#                                "vol_7d": "165121.9500000000",
#                                "high_30d": "90.0000000000",
#                                "low_30d": "3.2900000000",
#                                "avg_30d": "63.29681988451545",
#                                "vol_30d": "624566.3100000000",
#                                "high_6m": "250.0000000000",
#                                "low_6m": "3.2900000000",
#                                "avg_6m": "65.20315953363655",
#                                "vol_6m": "2740631.7100000000",
#                                "text": "[ 24 hours ] high 78.00 GBP, low 63.35 GBP, avg 67.56 GBP, volume 44884 GBP. [ 7 days ] high 78.00 GBP, low 60.00 GBP, avg 65.55 GBP, volume 165122 GBP. [ 30 days ] high 90.00 GBP, low 3.29 GBP, avg 63.30 GBP, volume 624566 GBP [ 6 months ] high 250.00 GBP, low 3.29 GBP, avg 65.20 GBP, volume 2740632 GBP."}}
