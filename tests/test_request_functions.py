from handle_request_functions import get_wufoo_data


def test_get_wufoo_data():
    url = ("https://j1masone.wufoo.com/api/v3/forms/cubes-project-proposal-"
           "submission/entries/json")
    test_total_submissions = 0
    test_form_entries = get_wufoo_data(url)

    for lists, entries in test_form_entries.items():
        for entry in entries:
            test_total_submissions += 1
    assert test_total_submissions >= 10
