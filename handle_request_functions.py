import requests
from requests.auth import HTTPBasicAuth
from secrets import wufoo_key
import sys


def get_wufoo_data(url_passed: str) -> requests.Response:
    try:
        response = requests.get(url_passed,
                                auth=HTTPBasicAuth(wufoo_key, "pass"))
    except requests.exceptions.InvalidURL:
        print(f"The URL {url_passed} had: Invalid URL Error")
        exit()
    except requests.exceptions.ConnectionError:
        print(f"The URL {url_passed} had: Connection Error")
        exit()

    _check_status_code(response)

    json_response = response.json()
    return json_response


def _check_status_code(response: requests.Response):
    if response.status_code != 200:
        print(
            f"Failed to get data, response code: {response.status_code} "
            f"and error message: {response.reason}"
        )
        sys.exit(-1)
    else:
        pass
