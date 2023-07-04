
query_string = 'abcdefghijklmn'
query_number = 12345678901234
replace_parameter = "無f替換變數"
replace_parameter += " WHERE {query_string}"
replace_parameter += " ORDER BY record_no DESC LIMIT {query_number}"
print(replace_parameter)


replace_parameter = "有f替換變數"
replace_parameter += f" WHERE {query_string}"
replace_parameter += f" ORDER BY record_no DESC LIMIT {query_number}"
print(replace_parameter)


table_columns = '(alpaca_name, training, duration, date)'
postgres_insert_query = f"""INSERT INTO alpaca_training {table_columns} VALUES (%s,%s,%s,%s)"""

print(postgres_insert_query)


import random

pretty_note = '♫♪♬'
pretty_text = ''

string_message = 'abcdefg'
for i in string_message:
    pretty_text += i
    pretty_text += random.choice(pretty_note)
    
print(pretty_text)



