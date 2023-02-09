import pytest
import sqlite3
from handle_request_functions import get_wufoo_data
from database_functions import connect_to_database, create_entry_table,\
    close_db


def test_get_wufoo_data():
    url = ("https://j1masone.wufoo.com/api/v3/forms/cubes-project-proposal-"
           "submission/entries/json")
    test_total_submissions = 0
    test_form_entries = get_wufoo_data(url)

    for lists, entries in test_form_entries.items():
        for entry in entries:
            test_total_submissions += 1

    assert test_total_submissions >= 10

    with pytest.raises(SystemExit) as system_error:
        url = ("https://j1masone.wufoo.com/api/v3/forms/c")
        test_form_entries = get_wufoo_data(url)
        assert system_error.type == SystemExit
        assert system_error.value.code == -1


def test_db_functions():
    test_db_name = 'test.db'
    test_table_name = 'test_table'

    db_connection, db_cursor = connect_to_database(test_db_name)
    create_entry_table(db_connection, db_cursor, test_table_name)
    query_test_table = db_cursor.execute(f'SELECT * FROM {test_table_name}')
    assert query_test_table is not None

    with pytest.raises(sqlite3.OperationalError) as db_error:
        db_cursor.execute("SELECT * FROM MISSING")
        assert db_error.type == sqlite3.OperationalError

    close_db(db_connection, db_cursor)
