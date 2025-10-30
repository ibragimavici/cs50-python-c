import requests
import json
import sys


def is_number(a):
    try:
        float(a)
        return True
    except ValueError:
        return False


if len(sys.argv) < 2 :
    raise ValueError("not the right amount of sys")

if not is_number(sys.argv[1]):
    raise ValueError("value is not a number")



try:
    how_much = float(sys.argv[1])

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")


    usd = response.json()["bpi"]["USD"]["rate_float"]
    result = usd * how_much
    result = "{:,.4f}".format(result)


    print("$", result, sep="")




except requests.RequestException:
    print("Requests Error.")
except ValueError:
    sys.exit()

