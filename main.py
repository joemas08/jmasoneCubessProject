import sys
import requests
from secrets import wufoo_key
from requests.auth import HTTPBasicAuth


def get_wufoo_data() -> list[dict[1]]:
    url = "https://j1masone.wufoo.com/api/v3/forms/cubes-project-proposal-submission/entries/json"
    response = requests.get(url, auth=HTTPBasicAuth(wufoo_key, 'pass'))

    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
        sys.exit(-1)

    json_response = response.json()
    return json_response


if __name__ == '__main__':
    form_entries = get_wufoo_data()

    print(form_entries)


