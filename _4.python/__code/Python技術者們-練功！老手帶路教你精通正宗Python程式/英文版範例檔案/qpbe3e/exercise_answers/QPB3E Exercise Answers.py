import sys

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

temperatures = []
with open('lab_05.txt') as infile:
     for row in infile:
        temperatures.append(float(row.strip()))


max_temp = max(temperatures)
min_temp = min(temperatures)
mean_temp = sum(temperatures)/len(temperatures)
# we'll need to sort to get the median temp
temperatures.sort()
median_temp = temperatures[len(temperatures)//2]
print("max = {}".format(max_temp))
print("min = {}".format(min_temp))
print("mean = {}".format(mean_temp))
print("median = {}".format(median_temp))

unique_temps = len(set(temperatures))

print("number of temps - {}".format(len(temperatures)))
print("number of unique temps - {}".format(unique_temps))

cubes = {x: x**3 for x in range(11, 16)}
print(cubes)

# ---------------------------------------------------------------------------------------

# ### QUICK CHECK: BOOLEANS AND TRUTHINESS
# Decide if the following statements are true or false: 1, 0, -1, [0], 1 and 0, 1 > 0 or []
# ```
# 1 -> True.
# 0 -> False.
# -1 - True.
# [0] - True, it's a list containing one item.
# 1 and 0 - False.
# 1 > 0 or [] - True.
# ```

# ### LAB: REFACTOR WORD_COUNT
# Rewrite the word count program to make it shorter. You may want to look at the string and list operations already discussed, as well as thinking about different ways to organize the code. You may also want to make it smarter, so that only alphabetic strings (not symbols or punctuation) count as words.

# File: word_count_refactored.py
""" Reads a file and returns the number of lines, words,
    and characters - similar to the UNIX wc utility
"""

# initialze counts
line_count = 0
word_count = 0
char_count = 0

# open the file
with  open('word_count.tst') as infile:
    for line in infile:
        line_count += 1
        char_count += len(line)
        words = line.split()
        word_count += len(words)

# print the answers using the format() method
print("File has {0} lines, {1} words, {2} characters".format(line_count, 
                                               word_count, char_count))

print("------------------------------------------------------------")  # 60個
# ## Chapter 9
print("------------------------------------------------------------")  # 60個

def my_funct(*params):
    for i in reversed(params):
        print(i)

my_funct(1,2,3,4)


# ### QUICK CHECK: MUTABLE FUNCTION PARAMETERS
# 
# What would be the result of changing a list or dictionary that was passed into a function as a parameter value? 
# 
# The changes would persist for future uses of the default parameter.
# 
# Which operations would be likely to create changes that would be visible outside the function? What steps might you take to minimize that risk?
# 
# Operations like adding and deleteing elements, as well as changing the value of an element. To minimize the risk, it's better not to use mutable types as default parameters.

# ### TRY THIS: GLOBAL VS LOCAL VARIABLES
# Assuming x = 5, what will be the value of x after calling funct_1() below executes? After calling funct_2()?
# ```
# def funct_1():
#     x = 3
# def funct_2():
#     global x
#     x = 2 
# ```    
# After calling `funct_1()` x will be unchanged; after `funct_2()` the value in the global x will be 2. 

# ### QUICK CHECK: GENERATOR FUNCTIONS
# What would you need to modify in the code for the function four() above to make it work for any number? What would you need to add to allow the starting point to also be set?
# 

def four(limit):
    x = 0 
    while x < limit:
        print("in generator, x =", x)
        yield x
        x += 1

for i in four(4):
    print(i)

def four(start, limit):
    x = start 
    while x < limit:
        print("in generator, x =", x)
        yield x
        x += 1

for i in four(1, 4):
    print(i)


# ### TRY THIS: DECORATORS
# How would you modify the code for the decorator function above to remove unneeded messages and enclose the return value of wrapped function in "<html>" and "</html>", so that myfunction("hello") would return "<html>hello<html>"?
#     
# This is a hard one, since in order to define a function that changes the return value we need to add an inner wrapper function to call the orginal function and add to the return value

def decorate(func):
    def wrapper_func(*args):
        def inner_wrapper(*args):
                return_value = func(*args)
                return "<html>{}<html>".format(return_value)
                
        return inner_wrapper(*args)
    return wrapper_func

@decorate
def myfunction(parameter):
    return parameter 

print(myfunction("Test"))


# ### LAB: USEFUL FUNCTIONS
# Looking back at the labs for chapters 6 and 7, refactor that code into functions for cleaning and processing the data. The goal should be that most of the logic is moved into functions. Use your own judgement as to the types of functions and parameters, but keep in mind that functions should do just one thing, and they should not have any side effects that carry over outside of the function.  

punct = str.maketrans("",  "", "!.,:;-?")

def clean_line(line):
    """changes case and removes punctuation"""
    # make all one case
    cleaned_line = line.lower()
        
    # remove punctuation
    cleaned_line = cleaned_line.translate(punct)
    return cleaned_line


def get_words(line):
    """splits line into words, and rejoins with newlines"""
    words = line.split()
    return "\n".join(words) + "\n"
     
    
with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    for line in infile:
        cleaned_line = clean_line(line)
                
        cleaned_words = get_words(cleaned_line)
        
        # write all words for line
        outfile.write(cleaned_words)


def count_words(words):
    """takes list of cleaned words, returns count dictionary"""
    word_count = {}
    for word in moby_words:
        count = word_count.setdefault(word, 0)
        word_count[word] += 1
    return word_count


def word_stats(word_count):
    """Takes word count dictionary and returns top and bottom five entries"""
    word_list = list(word_count.items())
    word_list.sort(key=lambda x: x[1])
    least_common = word_list[:5]
    most_common = word_list[-1:-6:-1]
    return most_common, least_common

moby_words = []
with open('moby_01_clean.txt') as infile:
    for word in infile:
        if word.strip():
            moby_words.append(word.strip())
        
word_count = count_words(moby_words)

most, least = word_stats(word_count)
print("Most common words:")
for word in most:
    print(word)
print("\naaa Least common words:")
for word in least:
    print(word)

print("------------------------------------------------------------")  # 60個
# ## Chapter 10
print("------------------------------------------------------------")  # 60個

# ### QUICK CHECK: MODULES
# Suppose you have a module called new_math that contains a function called new_divide. What are the ways that you might import and then use that function? What are the pros and cons of each?
# 
# ```
# import new_math
# new_math.new_divide(...)
# ```
# This is often preferred, since there will not be a clash between any identifiers in new_module and the importing namespace. However it's less convenient to type.
# 
# ```
# from new_math import new_divide
# new_divide(...)
# ```
# More convenient to use, but increases the chance of name clashes between identifiers in the module and the importing namespace.
# 
# Suppose that the new_math module contains a function call \_helper_math(). How will the underscore character affect the way that \_helper_math() is imported? 
# 
# It won't be imported if you use `from new_math import *`

# ### QUICK CHECK: NAMESPACES AND SCOPE
# Consider a variable `width` which is in the module make_window.py. In which of the following contexts is `width` in scope? 
# 
# 1. within the module itself,  
# 2. inside the resize() function in the module, 
# 3. within the script that imported the make_window.py module.
# 
# 1 and 2, but not 3

# ### LAB: CREATE A MODULE
# Package the functions that you created at the end of chapter 9 as a standalone module. While you can include code to run the module as the main program, the goal should be for the functions to be completely usable from another script. 
# 
# (no answer)

print("------------------------------------------------------------")  # 60個
# ## Chapter 11
print("------------------------------------------------------------")  # 60個

# File: word_count_program.py
""" Reads a file and returns the number of lines, words,
    and characters - similar to the UNIX wc utility
"""

def main():
    # initialze counts
    line_count = 0
    word_count = 0
    char_count = 0
    
    option = None
    params = sys.argv[1:]
    if len(params) > 1:
        # if more than one param, pop the first one as the option
        option = params.pop(0).lower().strip()
    filename = params[0]    # open the file
    with  open(filename) as infile:
        for line in infile:
            line_count += 1
            char_count += len(line)
            words = line.split()
            word_count += len(words)
    
    if option == "-c":
        print("File has {} characters".format(char_count))
    elif option == "-w":
        print("File has {} words".format(word_count))
    elif option == "-l":
        print("File has {} lines".format(line_count))
    else:
        # print the answers using the format() method
        print("File has {0} lines, {1} words, {2} characters".format(line_count, 
                                                       word_count, char_count))
"""
if __name__ == '__main__':
    main()
"""

print("------------------------------------------------------------")  # 60個
# ## Chapter 12
print("------------------------------------------------------------")  # 60個

import os.path
old_path = os.path.abspath('test.log')
print(old_path)
new_path = '{}.{}'.format(old_path, "old")
print(new_path)

import pathlib
path = pathlib.Path('test.log')
abs_path = path.resolve()
print(abs_path)
new_path = str(abs_path) + ".old"
print(new_path)

test_path = pathlib.Path(os.pardir)
print(test_path)
test_path.resolve()


# ### LAB: MORE FILE OPERATIONS
# How might you calculate the total size of all files ending with .txt that are not symlinks in a directory? If your first answer was using os.path, also try it with pathlib, and vice versa.

import pathlib
cur_path = pathlib.Path(".")

size = 0
for text_path in cur_path.glob("*.txt"):
    if not text_path.is_symlink():
        size += text_path.stat().st_size
        
print(size)


# Write some code that builds off your solution above to move the same .txt files in the question above to a new subdirectory called 'backup' in the same directory.

"""
import pathlib
cur_path = pathlib.Path(".")
new_path = cur_path.joinpath("backup")

size = 0
for text_path in cur_path.glob("*.txt"):
    if not text_path.is_symlink():
        size += text_path.stat().st_size
        text_path.rename(new_path.joinpath(text_path.name))
        
print(size)
"""
print("------------------------------------------------------------")  # 60個
# ## Chapter 13
print("------------------------------------------------------------")  # 60個

import mio

def main():
    mio.capture_output("myfile.txt")
    print("hello")
    print(1 + 3)
    mio.restore_output()
    
    mio.print_file("myfile.txt")
    
"""
if __name__ == '__main__':
    main()
"""

def main():
    # initialze counts
    line_count = 0
    word_count = 0
    char_count = 0
    filename = None
    
    option = None
    if len(sys.argv) > 1:
        params = sys.argv[1:]
        if params[0].startswith("-"):
        # if more than one param, pop the first one as the option
            option = params.pop(0).lower().strip()
        if params:
            filename = params[0]    # open the file
    file_mode = "r"
    if option == "-c":
        file_mode = "rb"
    if filename:
        infile =  open(filename, file_mode)
    else:
        infile = sys.stdin
    with infile:
        for line in infile:
            line_count += 1
            char_count += len(line)
            words = line.split()
            word_count += len(words)
    
    if option in ("-c", "-m"):
        print("File has {} characters".format(char_count))
    elif option == "-w":
        print("File has {} words".format(word_count))
    elif option == "-l":
        print("File has {} lines".format(line_count))
    else:
        # print the answers using the format() method
        print("File has {0} lines, {1} words, {2} characters".format(line_count, 
                                                       word_count, char_count))
"""
if __name__ == '__main__':
    main()
"""


punct = str.maketrans("",  "", "!.,:;-?")
class EmptyStringError(Exception):
    pass


def get_words(line):
    """splits line into words, and rejoins with newlines"""
    words = line.split()
    return "\n".join(words) + "\n"
     
    
with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    for line in infile:
        cleaned_line = clean_line(line)
                
        cleaned_words = get_words(cleaned_line)
        
        # write all words for line
        outfile.write(cleaned_words)


def count_words(words):
    """takes list of cleaned words, returns count dictionary"""
    word_count = {}
    for word in words:
        try:
            count = word_count.setdefault(word, 0)
        except TypeError:
            #if 'word' is not hashable, skip to next word.
            pass
        word_count[word] += 1
    return word_count


def word_stats(word_count):
    """Takes word count dictionary and returns top and bottom five entries"""
    word_list = list(word_count.items())
    word_list.sort(key=lambda x: x[1])
    try:
        least_common = word_list[:5]
        most_common = word_list[-1:-6:-1]
    except IndexError as e:
        # if list is empty or too short, just return list
        least_common = word_list
        most_common = list(reversed(word_list))
        
    return most_common, least_common

moby_words = []
with open('moby_01_clean.txt') as infile:
    for word in infile:
        if word.strip():
            moby_words.append(word.strip())
        
word_count = count_words(moby_words)

most, least = word_stats(word_count)
print("Most common words:")
for word in most:
    print(word)
print("\nbbb Least common words:")
for word in least:
    print(word)

print("------------------------------------------------------------")  # 60個
# ## Chapter 16
print("------------------------------------------------------------")  # 60個

import re

re.match(r": (?P<phone>(\+\d{2}-)?(\d\d\d-)?\d\d\d-\d\d\d\d)", ": +01-111-222-3333")
#or
re.match(r": (?P<phone>(\+\d{2}-)?(\d{3}-)?\d{3}-\d{4})", ": +01-111-222-3333")
#for 1 to 3 digit country codes:
re.match(r": (?P<phone>(\+\d{1,3}-)?(\d{3}-)?\d{3}-\d{4})", ": +011-111-222-3333")

def add_code(match_obj):
    return("+1 "+match_obj.group('phone'))

re.sub(r"(?P<phone>(\d{3}-)?\d{3}-\d{4})", add_code, "111-222-3333")

import re

test_numbers = ["+1 223-456-7890",
                "1-223-456-7890",
                "+1 223 456-7890",
                "(223) 456-7890",
                "1 223 456 7890",
                "223.456.7890",
               "1-989-111-2222"]

def return_number(match_obj):
    
    # validate number raise ValueError if not valid
    if not re.match(r"[2-9][0-8]\d", match_obj.group("area") ): 
        raise ValueError("invalid phone number area code {}".format(match_obj.group("area")))
    if not re.match(r"[2-9]\d\d", match_obj.group("exch") ):
        raise ValueError("invalid phone number exchange {}".format(match_obj.group("exch")))
        
    country = match_obj.group("country")
    if not country:
        country = "1"
        
    return("{}-{}-{}-{}".format(country, match_obj.group('area'), 
                                match_obj.group('exch'), match_obj.group('number')))

""" NG
regexp = re.compile(r"\+?(?P<country>\d{1,3})?[- .]?\(?(?P<area>\d{3})\)?[- .]?(?P<exch>(\d{3}))[- .](?P<number>\d{4})")
for number in test_numbers:
    print(regexp.sub(return_number, number))
"""

print("------------------------------------------------------------")  # 60個
# ## Chapter 17
print("------------------------------------------------------------")  # 60個

x = []
if isinstance(x, list):
    print("is list")

# exceptions.py
class EmptyStringError(Exception):
    pass

# cleaning.py
from word_count import EmptyStringError

punct = str.maketrans("",  "", "!.,:;-?")

def clean_line(line):
    """changes case and removes punctuation"""
    
    # raise exception if line is empty
    if not line.strip():
        raise EmptyStringError()
    # make all one case
    cleaned_line = line.lower()
        
    # remove punctuation
    cleaned_line = cleaned_line.translate(punct)
    return cleaned_line


def get_words(line):
    """splits line into words, and rejoins with newlines"""
    words = line.split()
    return "\n".join(words) + "\n"
   

# counter.py

def count_words(words):
    """takes list of cleaned words, returns count dictionary"""
    word_count = {}
    for word in moby_words:
        try:
            count = word_count.setdefault(word, 0)
        except TypeError:
            #if 'word' is not hashable, skip to next word.
            pass
        word_count[word] += 1
    return word_count


def word_stats(word_count):
    """Takes word count dictionary and returns top and bottom five entries"""
    word_list = list(word_count.items())
    word_list.sort(key=lambda x: x[1])
    try:
        least_common = word_list[:5]
        most_common = word_list[-1:-6:-1]
    except IndexError as e:
        # if list is empty or too short, just return list
        least_common = word_list
        most_common = list(reversed(word_list))
        
    return most_common, least_common


from word_count import clean_line, get_words, count_words, word_stats, EmptyStringError

with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    for line in infile:
        try:
            cleaned_line = clean_line(line)
        except EmptyStringError:
            continue
                
        cleaned_words = get_words(cleaned_line)
        
        # write all words for line
        outfile.write(cleaned_words)
        
moby_words = []
with open('moby_01_clean.txt') as infile:
    for word in infile:
        if word.strip():
            moby_words.append(word.strip())
        
word_count = count_words(moby_words)

most, least = word_stats(word_count)
print("Most common words:")
for word in most:
    print(word)
print("\nccc Least common words:")
for word in least:
    print(word)

import word_count
dir(word_count)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import datetime
import pathlib

FILE_PATTERN = "*.txt"
ARCHIVE = "archive"

"""
if __name__ == '__main__':
    
    date_string = datetime.date.today().strftime("%Y-%m-%d")

    cur_path = pathlib.Path(".")

    new_path = cur_path.joinpath(ARCHIVE, date_string)
    new_path.mkdir()                                    #A

    paths = cur_path.glob(FILE_PATTERN)

    for path in paths:
        path.rename(new_path.joinpath(path.name))
"""

import datetime
import pathlib
import zipfile

FILE_PATTERN = "*.txt"
ARCHIVE = "archive"

"""
if __name__ == '__main__':
    
    date_string = datetime.date.today().strftime("%Y-%m-%d")

    cur_path = pathlib.Path(".")
    paths = cur_path.glob(FILE_PATTERN)

    zip_file_path = cur_path.joinpath(ARCHIVE, date_string + ".zip")
    zip_file = zipfile.ZipFile(str(zip_file_path), "w")

    for path in paths:
        zip_file.write(str(path))
        path.unlink()
"""

import requests 
response = requests.get("http://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/heathrowdata.txt")

data = response.text
data_rows = []
rainfall = []
for row in data.split("\r\n")[7:]:
    fields = [x for x in row.split(" ") if x]
    data_rows.append(fields)
    rainfall.append(float(fields[5]))

print("Average rainfall = {} mm".format(sum(rainfall)/len(rainfall)))

import requests 
response = requests.get("https://data.cityofchicago.org/resource/6zsd-86xi.json?$where=date between '2015-01-10T12:00:00' and '2015-01-10T13:00:00'&arrest=true")

print(response.text)

print("------------------------------------------------------------")  # 60個

import json
import requests 

response = requests.get("https://data.cityofchicago.org/resource/6zsd-86xi.json?$where=date between '2015-01-10T12:00:00' and '2015-01-10T13:00:00'&arrest=true")

crime_data = json.loads(response.text)

with open("crime_all.json", "w") as outfile:
    json.dump(crime_data, outfile)

with open("crime_series.json", "w") as outfile:
    for record in crime_data:
        json.dump(record, outfile)
        outfile.write("\n")

with open("crime_all.json") as infile:
    crime_data_2 = json.load(infile)

crime_data_3 = []
with open("crime_series.json") as infile:
    for line in infile:
        crime_data_3 = json.loads(line)


import requests
import xmltodict

response = requests.get("https://graphical.weather.gov/xml/SOAP_server/ndfdXMLclient.php?whichClient=NDFDgen&lat=41.87&lon=+-87.65&product=glance")

parsed_dict = xmltodict.parse(response.text)
layout_key = parsed_dict['dwml']['data']['time-layout'][0]['layout-key']
forecast_temp = parsed_dict['dwml']['data']['parameters']['temperature'][0]['value'][0]
print(layout_key)
print(forecast_temp)

print("------------------------------------------------------------")  # 60個

import csv
import bs4

def read_html(filename):
    with open(filename) as html_file:
        html = html_file.read()
        return html


def parse_html(html):
    bs = bs4.BeautifulSoup(html, "html.parser")
    labels = [x.text for x in bs.select(".forecast-label")]
    forecasts = [x.text for x in bs.select(".forecast-text")]
    
    return list(zip(labels, forecasts))
    
def write_to_csv(data, outfilename):
    csv.writer(open(outfilename, "w")).writerows(data)
        
if __name__ == '__main__':
    html = read_html("forecast.html")
    values = parse_html(html)
    write_to_csv(values, "forecast.csv")
    print(values)

import json
import csv
import requests
""" NG
for sol in range(1830, 1863):
    response = requests.get("http://marsweather.ingenology.com/v1/archive/?sol={}&format=json".format(sol))
    result = json.loads(response.text)
    if not result['count']:
        continue
    weather = result['results'][0]
    print(weather)
    csv.DictWriter(open("mars_weather.csv", "a"), list(weather.keys())).writerow(weather)
"""

print("------------------------------------------------------------")  # 60個
# ## Chapter 24
print("------------------------------------------------------------")  # 60個

import pandas as pd
import numpy as np

# see text for these
calls = pd.read_csv("sales_calls.csv")
revenue = pd.read_csv("sales_revenue.csv")
calls_revenue = pd.merge(calls, revenue, on=['Territory', 'Month'])
calls_revenue['Call_Amount'] = calls_revenue.Amount/calls_revenue.Calls

# plot
calls_revenue[['Month', 'Call_Amount']].groupby(['Month']).mean().plot()

