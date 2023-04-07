
print('兩點距離')
x1, y1 = 0, 0
x2, y2 = 3, 4
distance = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
print('兩點距離 : ', distance) 
 


print('if and or')
year = 2024
isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(year, "is a leap year?", isLeapYear)

print('if and or')
number = 126

if number % 2 == 0 and number % 3 == 0:
    print(number, "is divisible by 2 and 3")

if number % 2 == 0 or number % 3 == 0:
    print(number, "is divisible by 2 or 3")

if (number % 2 == 0 or number % 3 == 0) and \
       not (number % 2 == 0 and number % 3 == 0):
    print(number, "divisible by 2 or 3, but not both")


print('if and or')
lottery = 35
guess = 35

# Get digits from lottery
lotteryDigit1 = lottery // 10
lotteryDigit2 = lottery % 10

# Get digits from guess
guessDigit1 = guess // 10
guessDigit2 = guess % 10

print("The lottery number is", lottery)

# Check the guess
if guess == lottery:
    print("Exact match: you win $10,000")
elif (guessDigit2 == lotteryDigit1 and guessDigit1 == lotteryDigit2):
    print("Match all digits: you win $3,000")
elif (guessDigit1 == lotteryDigit1 or guessDigit1 == lotteryDigit2 
        or guessDigit2 == lotteryDigit1 or guessDigit2 == lotteryDigit2):
    print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")



import random 

# Generate random numbers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)


number = random.randint(0, 100) 
number = random.randint(1, 100)


def bubbleSort(list):
    needNextPass = True
    
    k = 1
    while k < len(list) and needNextPass:
        # List may be sorted and next pass not needed
        needNextPass = False
        for i in range(len(list) - k): 
            if list[i] > list[i + 1]:
                # swap list[i] with list[i + 1]
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
          
                needNextPass = True # Next pass still needed

list = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
bubbleSort(list)
for v in list:
    print(v)




students = [
    ("John", "Smith", 96),
    ("Susan", "King", 76),
    ("Kim", "Yao", 99)
]
students.sort(key=lambda e: (e[1]))
print(students)
print(sorted(students, key = lambda t: (t[2]), reverse = True))

        
import time

startTime = time.time() # Get start time

#do something
#do something
#do something

endTime = time.time() # Get end time
testTime = int(endTime - startTime) # Get test time
print("Test time is", testTime, "seconds")


#test strip
#filename = input("Enter a filename: ").strip()

print('測試 strip()')
input_string = 'ABCDEFG       '
print('無strip <<<' + input_string + '>>>')
input_string = input_string.strip()
print('有strip <<<' + input_string + '>>>')

def printArea(width = 1, height = 2):
    area = width * height
    print("width:", width, "\theight:", height, "\tarea:", area)

printArea() # Default arguments width = 1 and height = 2
printArea(4, 2.5) # Positional arguments width = 4 and height = 2.5
printArea(height = 5, width = 3) # Keyword arguments width 
printArea(width = 1.2) # Default height = 2
printArea(height = 6.2) # Default widht = 1



a = 5
b = "Hello"
c = 0.15
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

a = "Why not to learn "
b = "Python?"

print(len(a))
print(a[2])
print(a[4:7])
print(a.replace("learn", "teach"))
print(a.split(" "))
print(a+b)




candyCan = ["apple", "strawberry", "grape", "mango"]

candyCan[1] = "peach"
print(candyCan)


candyCan = ["apple", "strawberry", "grape", "mango"]

candyCan.append("banana")
print(candyCan)


candyCan = ["apple", "strawberry", "grape", "mango"]

candyCan.insert(1, "orange")
print(candyCan)



candyCan = ["apple", "strawberry", "grape", "mango"]

print(candyCan[1])
print(candyCan[-1])
print(candyCan[1:3])



candyCan = ["apple", "strawberry", "grape", "mango"]

print(candyCan)
print(len(candyCan))
print(type(candyCan))

candyCan = ["apple", "strawberry", "grape", "mango"]

print("apple" in candyCan)
print("banana" in candyCan)


candyCan = ["apple", "strawberry", "grape", "mango"]

newCandy = ["banana", "orange"]
temp = candyCan + newCandy
print(temp)
print(candyCan)
print(newCandy)


candyCan = ("apple", "strawberry", "mango", "peach", "grape")

candyCan[1] = "banana"


candyCan = ("apple", "strawberry", "mango", "peach", "grape")

print(candyCan)
print(len(candyCan))

print(candyCan[0])
print(candyCan[1:3])

print(candyCan.count("mango"))
print(candyCan.index("mango"))




candyFlavor = {"apple", "strawberry", "mango", "mango"}
print(candyFlavor)

candyFlavor.add("orange")
print(candyFlavor)

candyFlavor.remove("orange")
print(candyFlavor)

newFlavor = {"apple", "banana"}
candyFlavor.update(newFlavor)
print(candyFlavor)



candyNumber = {"apple": 5, "strawberry": 10, "mango": 3}

print(candyNumber)

print(candyNumber["apple"])
candyNumber["apple"] = 6
print(candyNumber)

candyNumber["banana"] = 8
print(candyNumber)

candyNumber.pop("banana")
print(candyNumber)

print(candyNumber.keys())
print(candyNumber.values())
print(candyNumber.items())






#一維list
mylist = ["A", "B", "C", "D", "E"]

for elem in mylist:
    print(elem)
    












