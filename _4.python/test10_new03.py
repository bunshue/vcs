
#替代字串
TABLE_NAME = 'people'
SELECT = 'select * from %s order by age, name' % TABLE_NAME


print('select * from %s order by age, name' % TABLE_NAME)
print(SELECT)





key_id = 1234
SELECT = 'SELECT * FROM memos WHERE key=?', (str(key_id))
print(SELECT)



print('----------------------------------------------------------------------')	#70個

print('-' * 70)	#70個



