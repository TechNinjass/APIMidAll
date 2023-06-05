import pyodbc

__DRIVER = '{ODBC Driver 17 for SQL Server}'

__SERVER = 'ninjasnovo.database.windows.net'
__DATABASE = 'ninjasnovo'
__UID = 'CloudSAb47816c8'
__PASSWORD = 'Fatec1000@@@'
__CONNECTION_STR = (
    f'DRIVER={__DRIVER};SERVER={__SERVER};'
    f'DATABASE={__DATABASE};UID={__UID};PWD={__PASSWORD}'
)


__DRIVER_DEVELOPER = '{ODBC Driver 17 for SQL Server}'

__SERVER_DEVELOPER = 'ninjasnovo.database.windows.net'
__DATABASE_DEVELOPER = 'Migration_CI'
__UID_DEVELOPER = 'CloudSAb47816c8'
__PASSWORD_DEVELOPER = 'Fatec1000@@@' 
__CONNECTION_STR_DEVELOPER = (
    f'DRIVER={__DRIVER_DEVELOPER};SERVER={__SERVER_DEVELOPER};'
    f'DATABASE={__DATABASE_DEVELOPER};UID={__UID_DEVELOPER};PWD={__PASSWORD_DEVELOPER}'
)


def query(sql: str):
    with pyodbc.connect(__CONNECTION_STR) as cnxn:
        with cnxn.cursor() as cursor:
            return list(cursor.execute(sql))


def insert_values_file_transfer():
    values_file = query("SELECT name, size, format, date_upload, data_transfer, status FROM file_transfer")
    with pyodbc.connect(__CONNECTION_STR_DEVELOPER) as cnxn:
        with cnxn.cursor() as cursor:
            cursor.executemany("""
            INSERT INTO [file_transfer_developer] (name, size, format, date_upload, data_transfer, status)
            VALUES (?, ?, ?, ?, ?, ?)""", values_file)


insert_values_file_transfer()