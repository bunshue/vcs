# *運算式 Unpacking
pern = ('Vicky', 'Female', 65, 75, 93)   # Tuple
# Tuple做Unpacking
name, sex, *score = pern
#輸出相關的name & score
print(f'{name}: {score}')

