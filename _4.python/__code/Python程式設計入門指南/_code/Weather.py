NUMBER_OF_DAYS = 10
NUMBER_OF_HOURS = 24

# Initialize data
data = [] 
for i in range(NUMBER_OF_DAYS):
    data.append([])
    for j in range(NUMBER_OF_HOURS):
        data[i].append([])
        data[i][j].append(0) # Temperature value
        data[i][j].append(0) # Humidity value

print(data)
print('222')

filename2 = 'weather.txt'

print("讀取檔案 " + filename2)
with open(filename2, 'r', encoding = 'UTF-8') as f:
    #print(f.readline())  # 123中文字\n
    lines=f.readlines()

print(len(lines))
   
# Read input using input redirection from a file
for k in range(NUMBER_OF_DAYS * NUMBER_OF_HOURS):
    #line = input().strip().split()
    line = lines[k].strip().split()
    day = eval(line[0]) 
    hour = eval(line[1]) 
    temperature = eval(line[2]) 
    humidity = eval(line[3]) 
    data[day - 1][hour - 1][0] = temperature
    data[day - 1][hour - 1][1] = humidity

print('333')
# Find the average daily temperature and humidity
for i in range(NUMBER_OF_DAYS):
    dailyTemperatureTotal = 0
    dailyHumidityTotal = 0
    for j in range(NUMBER_OF_HOURS):
        dailyTemperatureTotal += data[i][j][0]
        dailyHumidityTotal += data[i][j][1]

    # Display result
    print("Day" + str(i) + "'s average temperature is " + str(dailyTemperatureTotal / NUMBER_OF_HOURS))
    print("Day " + str(i) + "'s average humidity is " + str(dailyHumidityTotal / NUMBER_OF_HOURS))


print(data)
