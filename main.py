from handle_request_functions import get_wufoo_data
from database_functions import connect_to_database, create_entry_table, \
    insert_wufoo_data_to_table, close_db
from gui_code import *
import sys

if __name__ == '__main__':  # comment to test workflow
    url = ("https://j1masone.wufoo.com/api/v3/forms/cubes-project-proposal-"
           "submission/entries/json")

    # form_entries = get_wufoo_data(url)

    database = 'form_submission.db'
    table_name = 'form_submissions'

    # db_connection, db_cursor = connect_to_database(database)
    # create_entry_table(db_connection, db_cursor, table_name)
    # insert_wufoo_data_to_table(db_connection, db_cursor,
    #                            form_entries, table_name)
    # close_db(db_connection, db_cursor)

    # Only need one Qapplication instance per application
    app = QApplication(sys.argv)

    window = MainWindow()
    # Windows are hidden by default
    window.show()

    app.exec_()
