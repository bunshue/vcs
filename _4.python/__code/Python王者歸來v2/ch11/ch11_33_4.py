# ch11_33_4.py
def mycar(cars,func):
    for car in cars:
        print(func(car))
    
dreamcars = ['porsche','rolls royce','maserati']
mycar(dreamcars, lambda carbrand:"My dream car is " + carbrand.title())

