import sqlite3

#取得一個資料庫內所有表單的名稱, list格式
def get_table_names(conn):
    table_names = []
    tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    for table in tables.fetchall():
        table_names.append(table[0])
    return table_names

#取得一個表單內所有欄位的名稱, list格式
def get_column_names(conn, table_name):
    column_names = []
    columns = conn.execute(f"PRAGMA table_info('{table_name}');").fetchall()
    for col in columns:
        column_names.append(col[1])
    return column_names

''' 綜合版, reserved
def get_database_info(conn):
    """Return a list of dicts containing the table name and columns for each table in the database."""
    table_dicts = []
    for table_name in get_table_names(conn):
        columns_names = get_column_names(conn, table_name)
        table_dicts.append({"table_name": table_name, "column_names": columns_names})
    print(type(table_dicts))
    return table_dicts
'''

db_filename  = 'ims_sql/db_ims.sqlite'
#db_filename = 'C:/_git/vcs/_1.data/______test_files1/_db/gasoline.sqlite'
db_filename  = 'db_20230703_113217.sqlite'

conn = sqlite3.connect(db_filename)

table_names = get_table_names(conn)
print(type(table_names))
talbe_names_length = len(table_names)
print('裡面有:', talbe_names_length, ' 個表單')
print('分別是:')
for table_name in table_names:
    print('表單:', table_name, end = '\t')
    column_names = get_column_names(conn, table_name)
    column_names_length = len(column_names)
    print('裡面有:', column_names_length, ' 個欄位', end = ' ')
    print('分別是:', end = ' ')
    for column_name in column_names:
        print(column_name, end = ' ')
    print()


conn.close()


print("程式執行完畢！")
