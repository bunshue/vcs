import os
import psycopg2

def query_rich_menu_setting(target_user_id):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    postgres_select_query = f"""SELECT * FROM user_rich_menu_setting WHERE line_user_id = '{target_user_id}';"""
    
    cursor.execute(postgres_select_query)
    target_user_id_setting = cursor.fetchone()
    
    if target_user_id_setting:
        print(target_user_id_setting)
        return target_user_id_setting[1:]
    else:
        return ('Google', 'Image')

def update_rich_menu_setting(target_user_id, col, setting):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    postgres_select_query = f"""SELECT * FROM user_rich_menu_setting WHERE line_user_id = '{target_user_id}';"""
    
    cursor.execute(postgres_select_query)
    
    if cursor.fetchone():
        postgres_update_query = f"UPDATE user_rich_menu_setting SET {col} = %s WHERE line_user_id = %s"
        cursor.execute(postgres_update_query, (setting, target_user_id))
        conn.commit()
        print(cursor.rowcount, "setting UPDATED")
        
    else:
        default_dict = {'line_user_id': target_user_id, 'engine': 'Google', 'method': 'Image'}
        default_dict[col] = setting
        postgres_insert_query = f"INSERT INTO user_rich_menu_setting (line_user_id, engine, method) VALUES (%s, %s, %s)"
        cursor.execute(postgres_insert_query, tuple(default_dict.values()))
        conn.commit()
        print(cursor.rowcount, "setting INSERTED")

def web_select_specific(condition):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    
    condition_query = []
    
    for key, value in condition.items():
        if value:
            condition_query.append(f"{key}={value}")
    if condition_query:
        condition_query = "WHERE " + ' AND '.join(condition_query)
    else:
        condition_query = ''
    
    postgres_select_query = f"""SELECT * FROM alpaca_training {condition_query} ORDER BY record_no;"""
    print(postgres_select_query)
    
    cursor.execute(postgres_select_query)

    dataclip = []
    temp = cursor.fetchmany(10)
    while temp:
        dataclip.extend(temp)
        temp = cursor.fetchmany(10)

    cursor.close()
    conn.close()

    return dataclip

def web_select_overall():
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    
    postgres_select_query = f"""SELECT * FROM alpaca_training ORDER BY record_no;"""
    
    cursor.execute(postgres_select_query)
    
    dataclip = []
    temp = cursor.fetchmany(10)
    while temp:
        dataclip.extend(temp)
        temp = cursor.fetchmany(10)
    
    cursor.close()
    conn.close()
    
    return dataclip

def line_select_record(column_query, number_query):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    postgres_select_query = "SELECT * FROM alpaca_training"
    if column_query:
        postgres_select_query += f" WHERE {column_query}"
    postgres_select_query += f" ORDER BY record_no DESC LIMIT {number_query}"
    print(postgres_select_query)
    cursor.execute(postgres_select_query)
    raw = cursor.fetchall()
    print(raw)
    dataclip = [(i[0], i[1], i[2], str(i[3]), str(i[4])) for i in raw]
    return dataclip
    

def line_select_distinct(column_name):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    
    postgres_select_query = f"""SELECT DISTINCT {column_name} FROM alpaca_training"""
    cursor.execute(postgres_select_query)
    raw = cursor.fetchall()
    print(raw)
    dataclip = [i[0] for i in raw]
    return dataclip

def line_insert_record(record_list):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    table_columns = '(alpaca_name, training, duration, date)'
    postgres_insert_query = f"""INSERT INTO alpaca_training {table_columns} VALUES (%s,%s,%s,%s)"""

    cursor.executemany(postgres_insert_query, record_list)
    conn.commit()

    result = f"恭喜您！ {cursor.rowcount} 筆資料成功匯入 alpaca_training 表單！"
    print(result)

    cursor.close()
    conn.close()
    
    return result