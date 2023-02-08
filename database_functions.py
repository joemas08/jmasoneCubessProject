import sqlite3
import requests


def connect_to_database(db_name: str):
    db_connection = None
    db_cursor = None

    try:
        # connect to a sqlite3 database (creates it if it doesn't exist)
        db_connection = sqlite3.connect(db_name)
        # creating cursor object to interact with connected database
        db_cursor = db_connection.cursor()

        print(f'- Database: {db_name} connected\n')

    except sqlite3.Error as db_error:
        print(f'A database error has occurred : \n [{db_error}]')
        exit()

    finally:
        return db_connection, db_cursor


def create_entry_table(db_connection: sqlite3.Connection,
                       db_cursor: sqlite3.Cursor, table_name: str):
    try:
        db_cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}(
                            entry_id TEXT PRIMARY KEY,
                            prefix TEXT NOT NULL,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            title TEXT NOT NULL,
                            org_name TEXT NOT NULL,
                            email TEXT NOT NULL,
                            org_site TEXT,
                            phone TEXT,
                            course_project TEXT,
                            guest_speaker TEXT,
                            site_visit TEXT,
                            job_shadow TEXT,
                            internships TEXT,
                            career_panel TEXT,
                            networking_event TEXT,
                            use_permission TEXT NOT NULL,
                            date_created TEXT,
                            created_by TEXT,
                            date_updated TEXT,
                            updated_by TEXT);''')

        # Clearing all data from table from previous runs of program
        db_cursor.execute(f'''DELETE FROM {table_name}''')

        print(f'~ {table_name} table has been created\n')

    except sqlite3.Error as db_error:
        print(f'A database error has occurred : {db_error}')
        close_db(db_connection, db_cursor)
        exit()


def insert_wufoo_data_to_table(db_connection: sqlite3.Connection,
                               db_cursor: sqlite3.Cursor,
                               form_entries: requests.Response,
                               table_name: str):
    try:
        for lists, entries in form_entries.items():
            for entry in entries:
                db_cursor.execute(f'''INSERT INTO {table_name} VALUES
                                  (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                                  ''',
                                  (entry.get('EntryId', 'No Entry'),
                                   entry.get('Field102', 'No Entry'),
                                   entry.get('Field104', 'No Entry'),
                                   entry.get('Field105', 'No Entry'),
                                   entry.get('Field106', 'No Entry'),
                                   entry.get('Field107', 'No Entry'),
                                   entry.get('Field109', 'No Entry'),
                                   entry.get('Field110', 'No Entry'),
                                   entry.get('Field111', 'No Entry'),
                                   entry.get('Field112', 'No Entry'),
                                   entry.get('Field113', 'No Entry'),
                                   entry.get('Field114', 'No Entry'),
                                   entry.get('Field115', 'No Entry'),
                                   entry.get('Field116', 'No Entry'),
                                   entry.get('Field117', 'No Entry'),
                                   entry.get('Field118', 'No Entry'),
                                   entry.get('Field213', 'No Entry'),
                                   entry.get('DateCreated', 'No Entry'),
                                   entry.get('CreatedBy', 'No Entry'),
                                   entry.get('DateUpdated', 'No Entry'),
                                   entry.get('UpdatedBy', 'No Entry')))
                db_connection.commit()
        print('~ Database: Database has been'
              ' populated with submission data\n')
    except sqlite3.Error as db_error:
        print(f'A database error has occurred : {db_error}')
        close_db(db_connection, db_cursor)
        exit()


def close_db(db_connection: sqlite3.Connection, db_cursor: sqlite3.Cursor):
    if db_cursor:
        db_connection.close()

    if db_connection:
        db_connection.close()
        print('~ Database: meteorite_db.db has been closed')
