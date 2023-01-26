import sys
import requests
from secret import wufoo_key
from requests.auth import HTTPBasicAuth


def get_wufoo_data() -> list[dict[1]]:
    url = ("https://j1masone.wufoo.com/api/v3/forms/cubes-project-proposal-"
           "submission/entries/json")
    response = requests.get(url, auth=HTTPBasicAuth(wufoo_key, 'pass'))

    if response.status_code != 200:
        print(f"Failed to get data, response code:{response.status_code}"
              "and error message: {response.reason} ")
        sys.exit(-1)

    json_response = response.json()
    return json_response


def send_form_data_to_file(form_passed: list[dict], file_passed: str):
    clear_file(file_passed)
    for lists, entries in form_passed.items():
        for entry in entries:
            for field, data in entry.items():
                if data == '':
                    data = 'No entry'
                with open(file_passed, 'a') as file:
                    file.write(f'{field}\t{data}\n')
            with open('entries.txt', 'a') as file:
                file.write('-' * 50 + '\n')


def clear_file(file_passed):
    with open(file_passed, 'a', encoding='UTF-8') as file:
        file.truncate(0)


if __name__ == '__main__':
    form_entries = get_wufoo_data()
    send_form_data_to_file(form_entries, 'entries.txt')
