import requests

date = "01.04.2019"

def download_exchange_rate(date):
    url = " http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"
    parameters = {"date": date}
    data = requests.get(url, params=parameters)
    return data.text

def parse_rates(data):
    header, names, *lines = data.splitlines()
    exchange_rates = {}
    for line in lines:
        _, _, amount, currency, value = line.replace(",", ".").split("|")
        exchange_rates[currency] = float(amount) / float(value)
    return exchange_rates
