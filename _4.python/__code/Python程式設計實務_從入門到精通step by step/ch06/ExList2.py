person = ["John", "Merry", "Mi", "Jason"]

addPerson = str(input("請輸入新增人員名字："))

if person.count(addPerson) == 0:
   person.insert(len(person) - 2, addPerson)

print("搜尋剛新增人員索引位置：", person.index(addPerson))

person1 = person.copy()
person.clear()

print("複製原串列：", person1)
print("原串列：", person)
