import requests
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "562ddaf40c95f5d58108"

printer = PrettyPrinter()


def get_data(endpoint):
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data from {url}")
        return None

def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    data = get_data(endpoint)

    if data:
        return sorted(data["results"].items())
    return []

def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get("currencySymbol", "")
        print(f"{_id} - {name} - {symbol}")

def get_exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    data = get_data(endpoint)

    if data:
        return list(data.values())[0]
    return None

def convert_currency(currency1, currency2, amount):
    rate = get_exchange_rate(currency1, currency2)

    if rate is None:
        print("Invalid currencies or exchange rate.")
        return

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount.")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount:.2f} {currency2}")

def main():
    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print("q - quit")
    print()

    while True:
        command = input("Enter a command: ").lower()

        if command == "q":
            break
        elif command == "list":
            currencies = get_currencies()
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert_currency(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            rate = get_exchange_rate(currency1, currency2)
            if rate is not None:
                print(f"Exchange rate: 1 {currency1} = {rate:.6f} {currency2}")
            else:
                print("Invalid currencies or exchange rate.")
        else:
            print("Unrecognized command!")

if __name__ == "__main__":
    main()
