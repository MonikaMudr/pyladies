import click
from requests_click import download_exchange_rate, parse_rates

@click.command()
@click.option("--currency", multiple=True, help="Zadej tripismenou zkratku meny")
@click.option("--date", help="Zadej datum ve formatu dd.mm.rrrr. Neni-li zadano, bude pouzit aktualni kurz")
@click.argument("amount", type=click.FLOAT)
def currency_converter(currency, date, amount):
    data = download_exchange_rate(date)
    exchange_rates = parse_rates(data)
    if currency:
        for item in currency:
            try:
                conversion = exchange_rates[item] * amount
                click.echo(f'{amount} CZK = {conversion} {item}')
            except KeyError:
                click.echo(f'{item} is unknown acronym')
    else:
        for keyword in exchange_rates:
            conversion = exchange_rates[keyword] * amount
            click.echo(f'{amount} CZK = {conversion} {keyword}')


if __name__ == "__main__":
    currency_converter()