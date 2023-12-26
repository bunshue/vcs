# ch4_19.py
name = '洪錦魁'
message = f"我是{name}"
print(message)

url = "https://maps.apis.com/json?city="
city = "taipei"
r = 1000
type = "school"
my_url = url + f"{city}&radius={r}&type={type}"
print(my_url)

score = 95.5
message = f"我的成績是 {score:10.2f}"
print(message)




