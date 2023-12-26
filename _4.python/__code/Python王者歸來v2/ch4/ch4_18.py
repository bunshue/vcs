# ch4_18.py
url = "https://maps.apis.com/json?city="
city = "taipei"
r = 1000
type = "school"
print(url + city + '&radius=' + str(r) + '&type=' + type)
print(url + "{}&radius={}&type={}".format(city, r, type))


