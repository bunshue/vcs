import sys

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

temperatures = []
with open('lab_05.txt') as infile:
     for row in infile:
        temperatures.append(float(row.strip()))


# In[88]:


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


# 看到這
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

# ### QUICK CHECK: FUNCTIONS AND PARAMETERS
# How would you write a function that could take any number of unnamed arguments and print their values out in reverse order?
# 
# What do you need to do to create a procedure or “void” function, that is a function with no return value?
# 
# Either don't return a value (use a bare return) or don't use a return statement at all.
# 
# What happens if you capture the return value of a function with a variable?
# 
# The only result is that you can use that value, whatever it might be.

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

# In[19]:

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

# ### QUICK CHECK:
# What is the significance of adding a "b" to the file open mode string?
# 
# It makes the file open in binary mode, reading and writng bytes, not characters.
# 
# Suppose you want to open a file named myfile.txt and write some additional data on the end of it. What command would you use to open myfile.txt? What command would you use to re-open the file to read from the beginning?
# 
# ```
# open("myfile.txt", "a")
# open("myfile.txt")
# ```

# ### TRY THIS: REDIRECTING INPUT AND OUTPUT
# Write some code to use the mio.py module above to capture all of the print output of a script to a file named "myfile.txt" and then reset the standard output to the screen, and print that file to screen.

# In[ ]:


# mio_test.py

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
# ## Chapter 15
print("------------------------------------------------------------")  # 60個

# ### TRY THIS: CLASSES AS RECORDS
# What code would you use to create a `Rectangle` class?

# In[236]:


class Rectangle:
    def __init__(self): 
        self.height = 1
        self.width = 2


# ### TRY THIS: INSTANCE VARIABLES AND METHODS
# Update the code for a `Rectangle` class so that you can set the dimensions when an instance is created, just as for the `Circle` class above. Also add an `area()` method.

# In[ ]:


class Rectangle:
    def __init__(self, width, height): 
        self.height = height
        self.width = width
        
    def area(self):
        return self.height * self.width


# ### TRY THIS: CLASS METHODS
# Write a class method similar to `total_area()`, but that would return the total circumference of all circles.

# In[242]:


class Circle:
    pi = 3.14159
    all_circles = []
    def __init__(self, radius):
        self.radius = radius
        self.__class__.all_circles.append(self)    
        
    def area(self):
        return self.radius * self.radius * Circle.pi
    
    def circumference(self):
        return 2 * self.radius * Circle.pi
    
    @classmethod
    def total_circumference(cls):
        """class method to total the circumference of all Circles """
        total = 0
        for c in cls.all_circles:
            total = total + c.circumference()
        return total



# ### TRY THIS: INHERITANCE
# Rewrite the code for a Rectangle class to inherit from Shape. Since squares and rectangles are related, would it make sense to inherit one from the other? If so, which would be the base class and which would inherit?
# 
# How would you write the code to add an area() method for the Square class? Should the area method be moved into the base Shape class and inherited by circle, square and rectangle? What issues would that cause?

# In[247]:


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
    


# It probably would make sense. Since squares are a special kind of rectangle, Square should inherit from the Rectangle class.
# 
# If square was specializes so that it had only one dimension x, then one would write:
# ```
# def area(self):
#     return self.x * self.x
# ```
# It make sense to put the area method in a Rectangle class that Square inherits from, but putting it in Shape wouldn't be very helpful, since different types of shapes have their own rules for calculating area, so every shape would be overriding the base area method anyway.

# ### TRY THIS: PRIVATE INSTANCE VARIABLES
# Modify the Rectangle class’s code to make the dimension variables private. What restriction will this impose on using the class?
# 
# The dimension variables will no longer be accessible outside the class via `.x` and `.y`.

# In[2]:


class Rectangle():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y


# ### TRY THIS: PROPERTIES
# Update the dimensions of the Rectangle class to be properties with getter and setters that will not allow negative sizes.
# 
# 

# In[5]:


class Rectangle():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    @property
    def x(self):
        return self.__x
            
    @x.setter
    def x(self, new_x):
        if new_x >= 0:
            self.__x = new_x
            
    @property
    def y(self):
        return self.__y
            
    @y.setter
    def y(self, new_y):
        if new_y >= 0:
            self.__y = new_y
            
my_rect = Rectangle(1,2)
print(my_rect.x, my_rect.y)
my_rect.x = 4
my_rect.y = 5
print(my_rect.x, my_rect.y)


# ### LAB: HTML CLASSES
# In this lab we’ll create classes to represent an HTML document. To keep things simple lets just assume that each element can contain only text and one sub-element. So the `<html>` element will only contain a `<body>` element, and the `<body>` element will contain (optional)text and a `<p>` element, which will contain only text. 
#   
# The key feature to implement is the `__str__()` method, which will in turn call its sub-element's `__str__()` method, so that the entire document is returned when the str() function is called on an `<html>` element. We can assume that any text comes before the subelement.
#     
# Example output from using the classes:
# ```
# para = p(text="this is some body text")
# doc_body = body(text="This is the body", subelement=para)
# doc = html(subelement=doc_body)
# print(doc)
# 
# <html>
# <body>
# This is the body
# <p>
# this is some body text
# </p>
# </body>
# </html>
# ```

# In[39]:


class element:
    def __init__(self, text=None, subelement=None):
        self.subelement = subelement
        self.text = text
        
    def __str__(self):
        value = "<{}>\n".format(self.__class__.__name__)
        if self.text:
            value += "{}\n".format(self.text)
        if self.subelement:
            value += str(self.subelement)
        value += "</{}>\n".format(self.__class__.__name__)
        return value

class html(element):
    def __init__ (self, text=None, subelement=None):
        super().__init__(text, subelement)
    def __str__(self):
        return super().__str__()
        
class body(element):
    def __init__ (self, text=None, subelement=None):
        return super().__init__(text, subelement)
    def __str__(self):
        return super().__str__()
        
class p(element):
    def __init__(self, text=None, subelement=None):
        super().__init__(text, subelement)
    def __str__(self):
        return super().__str__()
        
        
para = p(text="this is some body text")
doc_body = body(text="This is the body", subelement=para)
doc = html(subelement=doc_body)
print(doc)

print("------------------------------------------------------------")  # 60個
# ## Chapter 16
print("------------------------------------------------------------")  # 60個

# ### QUICK CHECK: SPECIAL CHARACTERS IN REGULAR EXPRESSIONS
# What regular expression would you use to match strings which represent the numbers -5 through 5?
# 
# `r"-{0,1}[0-5]"` will match strings which represent the numbers -5 through 5.
# 
# What regular expression would you use to match a hexadecimal digit? Assume that allowed hexadecimal digits are 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, a, B, b, C, c, D, d, E, e, F, and f.
# 
# `r"[0-9A-Fa-f]"`
# 

# ### TRY THIS: EXTRACTING MATCHED TEXT
# Making international calls usually requires a '+' and the country code. Assuming that the country code will be two digits, how would you modify the code above to extract the plus and the country code as part of the number. (Again, not all numbers will have a country code.) How would you make it handle country codes of one to three digits?

# In[296]:

import re

re.match(r": (?P<phone>(\+\d{2}-)?(\d\d\d-)?\d\d\d-\d\d\d\d)", ": +01-111-222-3333")
#or
re.match(r": (?P<phone>(\+\d{2}-)?(\d{3}-)?\d{3}-\d{4})", ": +01-111-222-3333")
#for 1 to 3 digit country codes:
re.match(r": (?P<phone>(\+\d{1,3}-)?(\d{3}-)?\d{3}-\d{4})", ": +011-111-222-3333")


# ### TRY THIS: REPLACING TEXT
# In the checkpoint above you extended a phone number regular expression to also recognize a country code. How would you now use a function to make any numbers that didn’t have a country code now have '+1' (the country code for the US and Canada)?

# In[286]:


def add_code(match_obj):
    return("+1 "+match_obj.group('phone'))

re.sub(r"(?P<phone>(\d{3}-)?\d{3}-\d{4})", add_code, "111-222-3333")


# ### LAB 16: PHONE NUMBER NORMALIZER
# In the USA and Canada phone numbers consist of 10 digits, usually separated into a 3 digit area code, a 3 digit exchange code, and 4 digit station code. As mentioned above they may or may not be preceded by +1, the country code. However, in practice there are many ways of formatting a phone number: (NNN) NNN-NNNN, NNN-NNN-NNNN, NNN NNN-NNNN, NNN.NNN.NNNN, and NNN NNN NNNN, to name a few. And the country code may or may not be present, and may or may not have a plus, and is usually (not always) separated from the number by a space or dash. Whew!
# In this lab the task is to create a phone number normalizer that will take any of the formats mentioned above and return a normalized phone number 1-NNN-NNN-NNNN. 
# The following are all possible phone numbers:
#     
# +1 223-456-7890	
# 1-223-456-7890	
# +1 223 456-7890
# (223) 456-7890	
# 1 223 456 7890	
# 223.456.7890
# 
# Bonus: The first digit of the area code and the exchange code can only be 2-9, and the second digit of an area code can’t be 9. Use this information to validate the input and return a `ValueError` Exception of “invalid phone number” if the number is invalid.

# In[4]:


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

# ### QUICK CHECK: TYPES
# Suppose you wanted to make sure that object x was a list before you tried appending to it? What code would you use? What would be the difference between using type() and isinstance()? Would this be the LBYL or EAFP of programming? What other options might you have besides checking the type explicitly? 
# 
# ```
# x = []
# if isinstance(x, list):
#     print("is list")
# ```
# Using `type` would only get lists, not anything that subclassed lists. Either way it's LBYL programming. 
# 
# You might also wrap the append in a try... except block and catch TypeError exceptions.

# In[249]:


x = []
if isinstance(x, list):
    print("is list")


# ### QUICK CHECK: __GETITEM__
# The example use of \__getitem__ above is very limited and will not work correctly in many situations. What are some cases where the implementation above will fail or work incorrectly?
# 
# The implementation of will not work if you try to access an item directly by index, nor can you move backwards. 

# ### TRY THIS: IMPLEMENTING LIST SPECIAL METHODS
# Try implementing the `__len__` and `__delitem__` special methods listed above, and an `append` method. 

# In[37]:


class TypedList:
    def __init__(self, example_element, initial_list=[]):
        self.type = type(example_element)
        if not isinstance(initial_list, list):
            raise TypeError("Second argument of TypedList must " 
                            "be a list.")
        for element in initial_list: 
            self.__check(element)
        self.elements = initial_list[:]
    def __check(self, element):
        if type(element) != self.type:
            raise TypeError("Attempted to add an element of " 
                            "incorrect type to a typed list.")
    def __setitem__(self, i, element):
        self.__check(element)
        self.elements[i] = element
    def __getitem__(self, i):
        return self.elements[i]

    # added methods
    def __delitem__(self, i):
        del self.elements[i]
    def __len__(self):
        return len(self.elements)
    def append(self, element):
        self.__check(element)
        self.elements.append(element)

x = TypedList(1, [1,2,3])
print(len(x))
x.append(1)
del x[2]

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
     


# In[219]:


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




# In[1]:


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


# ### TRY THIS: ACCESSING AN API
# Write some code to fetch some data from the city of Chicago site used above. Look at the fields mentioned in the results and see if you can select on records based on another field in combination with the date range.

# In[45]:


import requests 
response = requests.get("https://data.cityofchicago.org/resource/6zsd-86xi.json?$where=date between '2015-01-10T12:00:00' and '2015-01-10T13:00:00'&arrest=true")

print(response.text)
                        


# ### TRY THIS: SAVING SOME JSON CRIME DATA
# Modify the code you wrote to fetch Chicago crime data in section 22.2 above to convert the fetched data from a JSON formatted string to Python object. Then see if you can save the crime events both as a series of separate JSON objects in one fine and as one JSON object in another file. Then see what code is needed to load each file.

# In[51]:


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


# ### TRY THIS: FETCHING AND PARSING XML
# Write the code to pull the Chicago XML weather forecast from https://graphical.weather.gov/xml/SOAP_server/ndfdXMLclient.php?whichClient=NDFDgen&lat=41.87&lon=+-87.65&product=glance. The use xmltodict to parse the xml into a Python dictionary and extract tomorrow’s fordeecast maximum temperature. Hint: to match up time layouts and values, compare the layout-key value of the first time-layout section and the time-layout attribute of the temperature element of the parameters element.

# In[ ]:


import requests
import xmltodict

response = requests.get("https://graphical.weather.gov/xml/SOAP_server/ndfdXMLclient.php?whichClient=NDFDgen&lat=41.87&lon=+-87.65&product=glance")

parsed_dict = xmltodict.parse(response.text)
layout_key = parsed_dict['dwml']['data']['time-layout'][0]['layout-key']
forecast_temp = parsed_dict['dwml']['data']['parameters']['temperature'][0]['value'][0]
print(layout_key)
print(forecast_temp)


# ### TRY THIS: PARSING HTML
# Given the file forecast.html (which can also be found with the code on this book’s web site), write a script using Beautiful Soup that will extract the data and save it as a CSV file.

# In[35]:


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

for sol in range(1830, 1863):
    response = requests.get("http://marsweather.ingenology.com/v1/archive/?sol={}&format=json".format(sol))
    result = json.loads(response.text)
    if not result['count']:
        continue
    weather = result['results'][0]
    print(weather)
    csv.DictWriter(open("mars_weather.csv", "a"), list(weather.keys())).writerow(weather)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# ## Chapter 23
print("------------------------------------------------------------")  # 60個

import sqlite3

conn = sqlite3.connect("datafile.db")

cursor = conn.cursor()

# 建立表單 weather
cursor.execute("""create table weather (id integer primary key, state text, state_code text,
              year_text text, year_code text, avg_max_temp real,  max_temp_count integer, 
              max_temp_low real, max_temp_high real,
              avg_min_temp real, min_temp_count integer,
              min_temp_low real, min_temp_high real,
              heat_index real, heat_index_count integer, 
              heat_index_low real, heat_index_high real,
              heat_index_coverage text)
              """)
conn.commit()

# You could add a state table and only store each state's ID field in the weather database.

# ### TRY THIS: USING AN ORM
# Using the database from section 22.3 above, write a SQLAlchemy class to map to the data table and use it to read the records from the table. 

from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker

dbPath = 'datafile.db'
engine = create_engine('sqlite:///%s' % dbPath)
metadata = MetaData(engine)
weather  = Table('weather', metadata, 
                Column('id', Integer, primary_key=True),
                Column("state", String),
                Column("state_code", String),
                Column("year_text", String ),
                Column("year_code", String), 
                Column("avg_max_temp", Float),
                Column("max_temp_count", Integer),
                Column("max_temp_low", Float),
                Column("max_temp_high", Float),
                Column("avg_min_temp", Float), 
                Column("min_temp_count", Integer),
                Column("min_temp_low", Float), 
                Column("min_temp_high", Float),
                Column("heat_index", Float), 
                Column("heat_index_count", Integer),
                Column("heat_index_low", Float), 
                Column("heat_index_high", Float),
                Column("heat_index_coverage", String)
                )
Session = sessionmaker(bind=engine)
session = Session()
result = session.execute(select([weather]))
for row in result:
    print(row)

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

