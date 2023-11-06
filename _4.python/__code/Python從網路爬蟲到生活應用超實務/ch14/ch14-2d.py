import twstock

data = twstock.realtime.get("2330")
print(data)
print("----------------------------")
data = twstock.realtime.get(['2330', '2337', '2409'])
print(data)


