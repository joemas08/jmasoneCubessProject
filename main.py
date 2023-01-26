from handle_request_functions import get_wufoo_data
from file_functions import send_form_data_to_file


if __name__ == '__main__':
    url = ("https://j1masone.wufoo.com/api/v3/forms/cubes-project-proposal-"
           "submission/entries/json")
    form_entries = get_wufoo_data(url)
    send_form_data_to_file(form_entries, 'entries.txt')
