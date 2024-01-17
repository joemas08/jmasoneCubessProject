import pytest
import sqlite3
from handle_request_functions import get_wufoo_data
from database_functions import (
    connect_to_database,
    create_entry_table,
    close_db,
    insert_wufoo_data_to_table,
)


def test_get_wufoo_data():
    url = (
        "https://j1masone.wufoo.com/api/v3/forms/cubes-project-proposal-"
        "submission/entries/json"
    )
    test_total_submissions = 0
    test_form_entries = get_wufoo_data(url)

    for lists, entries in test_form_entries.items():
        for entry in entries:
            test_total_submissions += 1

    assert test_total_submissions >= 10

    with pytest.raises(SystemExit) as system_error:
        url = "https://j1masone.wufoo.com/api/v3/forms/c"
        test_form_entries = get_wufoo_data(url)
        assert system_error.type == SystemExit
        assert system_error.value.code == -1


def test_create_table():
    test_db_name = "test.db"
    test_table_name = "test_table"

    db_connection, db_cursor = connect_to_database(test_db_name)
    create_entry_table(db_connection, db_cursor, test_table_name)
    query_test_table = db_cursor.execute(f"SELECT * FROM {test_table_name}")
    assert query_test_table is not None

    with pytest.raises(sqlite3.OperationalError) as db_error:
        db_cursor.execute("SELECT * FROM MISSING")
        assert db_error.type == sqlite3.OperationalError

    close_db(db_connection, db_cursor)


def test_data_in_table():
    test_db_name = "test.db"
    test_table_name = "test_table"

    db_connection, db_cursor = connect_to_database(test_db_name)
    create_entry_table(db_connection, db_cursor, test_table_name)
    fake_form = {
        "entries": [
            {
                "EntryId": "1",
                "Field102": "Mr.",
                "Field104": "John",
                "Field105": "Doe",
                "Field106": "Supreme Leader",
                "Field107": "Generic Name Co.",
                "Field109": "sample@vanilla.com",
                "Field110": "No entry",
                "Field111": "5555555555",
                "Field112": "No entry",
                "Field113": "Guest Speaker",
                "Field114": "No entry",
                "Field115": "No entry",
                "Field116": "No entry",
                "Field117": "No entry",
                "Field118": "No entry",
                "Field213": "Yes",
                "DateCreated": "2023-01-24 13:13:21",
                "CreatedBy": "public",
                "DateUpdated": "No entry",
                "UpdatedBy": "None",
            }
        ]
    }
    insert_wufoo_data_to_table(db_connection, db_cursor,
                               fake_form, test_table_name)
    query_test_table = db_cursor.execute(
        f"SELECT * FROM {test_table_name} "
        f'WHERE first_name IN ("John") AND '
        f'last_name IN ("Doe")'
    )

    results = query_test_table.fetchall()
    assert results[0][0] == "1"
    assert results[0][1] == "Mr."
    assert results[0][2] == "John"
    assert results[0][3] == "Doe"
    assert results[0][17] == "2023-01-24 13:13:21"
    assert results[0][20] == "None"

    close_db(db_connection, db_cursor)
