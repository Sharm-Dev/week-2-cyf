import requests

def get_lucky_number(api, fromWhere):
    try:
        res = requests.get(api + fromWhere)
        res.raise_for_status()
    except requests.exceptions.HTTPError:
        return "Something went wrong, fix and try again."

    return res.text