import requests

NUMBERS_API_ENDPOINT = "http://numbersapi.com"


def get_fact_for_number(number):
    try:
        res = requests.get(f"{NUMBERS_API_ENDPOINT}/{number}")
        res.raise_for_status()
    except requests.exceptions.HTTPError:
        return "No fact is available - problems calling the upstream service!"

    return res.text
