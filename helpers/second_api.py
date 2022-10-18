import requests

def get_worst_food(api,fromWhere, errMessage):
    try:
        res = requests.get(api + fromWhere)
        res.raise_for_status()
    except requests.exceptions.HTTPError:
        return errMessage

    return res.text
