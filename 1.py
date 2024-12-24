import requests
import json
import datetime

def get_nbu_rates(start_date, end_date, valcode=''):

    url = 'https://bank.gov.ua/NBU_Exchange/exchange_site'
    params = {
        'start': start_date,
        'end': end_date,
        'valcode': valcode,
        'sort': 'exchangedate',
        'order': 'desc',
        'json': ''
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return json.loads(response.text)
today = datetime.date.today()
last_week = today - datetime.timedelta(days=7)
start_date = last_week.strftime('%Y%m%d')
end_date = today.strftime('%Y%m%d')
rates = get_nbu_rates(start_date, end_date, 'USD')
for rate in rates:
    print(f"Дата: {rate['exchangedate']}, Курс USD: {rate['rate']}")