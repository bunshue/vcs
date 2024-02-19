
import sys


from math import sqrt
sqrt(16)



from cmath import sqrt
sqrt(16)


from math import sqrt
sqrt(4)





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


# In[90]:


unique_temps = len(set(temperatures))

print("number of temps - {}".format(len(temperatures)))
print("number of unique temps - {}".format(unique_temps))

cubes = {x: x**3 for x in range(11, 16)}
print(cubes)


看到這
---------------------------------------------------------------------------------------



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

# In[ ]:


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


# ## Chapter 9

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

# In[157]:


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

# In[161]:


def four(limit):
    x = 0 
    while x < limit:
        print("in generator, x =", x)
        yield x
        x += 1

for i in four(4):
    print(i)



# In[162]:


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

# In[205]:


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

# In[213]:


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


# In[219]:


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
print("\nLeast common words:")
for word in least:
    print(word)


# ## Chapter 10

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

# ## Chapter 11

# ### TRY THIS: MAKING A SCRIPT EXECUTABLE
# Experiment with executing scripts on your platform. Also try to redirect input and output into and out of your scripts.
# 
# (no answer)

# ### QUICK CHECK: PROGRAMS AND MODULES
# What issue is the use of if `__name__ == "__main__":` meant to avoid, and how does it do that? Can you think of any other way to avoid this issue?
# 
# When Python loads a module all of its code is executed. By using the pattern above you can have certain code run only if it’s being executed as the main script file.

# ### LAB: CREATING A PROGRAM
# In chapter 8, we created a version of the UNIX wc utility to count the lines, words, and characters in a file.  Now that we have more tools at our disposal, lets refactor that program to make it work more like the original. In particular, it should have options to show only lines (-l), only words (-w), and only characters (-c). If none of those options are given, all three stats will be displayed. But if any one of them is present, then only the specified stats will be shown.
# 
# For an extra challenge, have a look at the man page for wc on a Linux/UNIX system and add the -L to show the longest line length. Feel free to try to implement the complete behavior as listed in the man page and test it against your system’s wc utility.

# In[13]:


# File: word_count_program.py
""" Reads a file and returns the number of lines, words,
    and characters - similar to the UNIX wc utility
"""
import sys


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

if __name__ == '__main__':
    main()


# ## Chapter 12

# ### QUICK CHECK: MANIPULATING PATHS
# How would you use the os module’s functions to take a path to a file called `test.log` and create a new file path in the same directory for a file called `test.log.old`? How would you do the same thing using the pathlib module?
# 
# What path would you get if you created a pathlib Path object from os.pardir? Try it and find out.

# In[170]:


import os.path
old_path = os.path.abspath('test.log')
print(old_path)
new_path = '{}.{}'.format(old_path, "old")
print(new_path)


# In[190]:


import pathlib
path = pathlib.Path('test.log')
abs_path = path.resolve()
print(abs_path)
new_path = str(abs_path) + ".old"
print(new_path)


# In[194]:


test_path = pathlib.Path(os.pardir)
print(test_path)
test_path.resolve()


# ### LAB: MORE FILE OPERATIONS
# How might you calculate the total size of all files ending with .txt that are not symlinks in a directory? If your first answer was using os.path, also try it with pathlib, and vice versa.

# In[16]:


import pathlib
cur_path = pathlib.Path(".")

size = 0
for text_path in cur_path.glob("*.txt"):
    if not text_path.is_symlink():
        size += text_path.stat().st_size
        
print(size)


# Write some code that builds off your solution above to move the same .txt files in the question above to a new subdirectory called 'backup' in the same directory.

# In[19]:


import pathlib
cur_path = pathlib.Path(".")
new_path = cur_path.joinpath("backup")

size = 0
for text_path in cur_path.glob("*.txt"):
    if not text_path.is_symlink():
        size += text_path.stat().st_size
        text_path.rename(new_path.joinpath(text_path.name))
        
print(size)


# ## Chapter 13

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
    
    
if __name__ == '__main__':
    main()


# ### QUICK CHECK: STRUCT
# What use cases can you think of where the struct module would be useful for either reading or writing binary data?
# 
# * You are trying to read/write from a binary format application file, or image file.
# * You are reading from some external interface, e.g., a thermometer or accelerometer, and want to save the raw dat exactly as it was transmitted.
# 

# ### QUICK CHECK: PICKLES
# Think about why a pickle would be a good solution for the following use cases, or why not: A) saving some state variables from one on run to the next; B) keeping a high score list for a game; C) storing user names and passwords; D) storing a large dictionary of English terms.
# 
# A & B would be reasonable, although pickles are not secure. 
# 
# C & D would not be good, the lack of security would be a big problem for C, and for D there would be a need to load the entire pickle into memory. 

# ### QUICK CHECK: SHELVE
# Using a shelf object looks very much like using a dictionary. In what ways is using a shelf object different? What disadvantages would you expect there to be in using a shelf object?
# 
# The key difference is that the objects are stored on disk, not in memory. With very large amounts of data, particularly with lots of inserts and/or deletes, you would expect disk access to make things slow.

# ### LAB: FINAL FIXES TO WC
# If you look at the man page for the wc utility you will see that there are two command line options which do very similar things. -c makes the utility count the bytes in the file, while -m makes it count characters (which in the case of some Unicode characters can be two or more bytes long). In addition, if a file is given it should read from and process that file, but if no file is given, it should read from and process stdin.
# 
# Rewrite your version of the `wc` utility to implement both the distinction between bytes and characters and the ability to read from files and standard input.

# In[20]:


# File: word_count_program_stdin.py
""" Reads a file and returns the number of lines, words,
    and characters - similar to the UNIX wc utility
"""
import sys


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

if __name__ == '__main__':
    main()


# ## Chapter 14

# ### TRY THIS: CATCHING EXCEPTIONS
# Write some code that gets two numbers from the user and divides the first by the second. Check for and catch the exception that occurs if the second number is zero (ZeroDivisionError).

# In[231]:


# the code of your program should do the following
x = int(input("Please enter an integer: "))
y = int(input("Please enter another integer: "))

try:
    z = x / y
except ZeroDivisionError as e:
    print("Can't divide by zero.")


# ### QUICK CHECK: EXCEPTIONS AS CLASSES
# If `MyError` inherits from `Exception`, what will be the difference between `except Exception as e` and `except MyError as e`?
# 
# The first will catch any exception that inherits from `Exception`, i.e., most of them, while the second will only catch `MyError` exceptions.

# ### TRY THIS: THE ASSERT STATEMENT
# Write a simple program which gets a number from the user and then uses the assert statement to raise an exception if the number is zero. Test to make sure the assert fires, then turn it off using one of the methods mentioned above.

# In[222]:


# the code of your program should do the following
x = int(input("Please enter a non-zero integer: "))

assert x != 0, "Integer can not be zero."


# ### QUICK CHECK: EXCEPTIONS
# Do Python exceptions force a program to halt?
# 
# No, if they are caught and handled correctly the program won't need to halt.
# 
# Suppose you wanted accessing a dictionary `x` to always return `None` if a key didn’t exist in the dictionary (i.e., if `KeyError` exception was raised)? What code would you use to achieve that?
# 

# In[ ]:


try:
    x = my_dict[some_key]
except KeyError as e:
    x = None
    


# ### TRY THIS: EXCEPTIONS
# What code would you use to create a custom ValueTooLarge exception and raise that exception if the variable x is over 1000?

# In[163]:


class ValueTooLarge(Exception):
    pass

x = 1001
if x > 1000:
    raise ValueTooLarge()


# ### QUICK CHECK: CONTEXT MANAGERS
# Assume you are using a context manager in a script that reads and/or writes several files. Which of the following approaches do you think would be the best? A) put the entire script in a block managed by a `with` statement; B) Use one `with` statement for all file reads and another for all file writes; C) a `with` statement each time you read a file or write a file, i.e., for each line; D) use a `with` statement for each file that you read or write.
# 
# Probably D is the best - since part of what the context manager does for file access is to make sure that a file is closed, it would probably make sense to use a separate w`with` for each case where you open a file for reading or writing.

# ### LAB: CUSTOM EXCEPTIONS
# Think about the module you wrote in chapter 9 to count word frequencies. What errors might reasonably occur in those functions? Rewrite the code to handle those exception conditions appropriately. 

# In[213]:


punct = str.maketrans("",  "", "!.,:;-?")
class EmptyStringError(Exception):
    pass

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
     
    
with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    for line in infile:
        cleaned_line = clean_line(line)
                
        cleaned_words = get_words(cleaned_line)
        
        # write all words for line
        outfile.write(cleaned_words)


# In[2]:


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
print("\nLeast common words:")
for word in least:
    print(word)


# ## Chapter 15

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


# ## Chapter 16

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


regexp = re.compile(r"\+?(?P<country>\d{1,3})?[- .]?\(?(?P<area>\d{3})\)?[- .]?(?P<exch>(\d{3}))[- .](?P<number>\d{4})")
for number in test_numbers:
    print(regexp.sub(return_number, number))


# ## Chapter 17

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


# ### QUICK CHECK: SPECIAL METHOD ATTRIBUTES AND SUBCLASSING EXISTING TYPES
# Suppose you wanted a dictionary-like type that only allowed strings as keys (maybe to make it work like a shelf object as described in Chapter 13). What options would you have for creating such a class? What would be the advantages and disadvantages of each?
# 
# You could use the same approach as we did for typed list and inherit from the UserDict class. You could also inherit directly from dict, or you could implement all of the dict functionality yourself. 
# 
# Implementing everything yourself gives the most control, but is the most work, and will be most prone to bugs. If the changes you need to make are small (in this case, just checking the type before adding a key), it might make the most sense to inherit directly from dict. On the other hand, inheriting from UserDict is probably the safest, since the internal dict object will continue to be a regular dict, which is a highly optimized and mature implementation.

# ## Chapter 18

# ### QUICK CHECK: PACKAGES
# Suppose you are writing a package that will take a URL, retrieve all images on the page pointed to by that URL, resize them to a standard size, and store them. Leaving aside the exact details of how each of these functions will be coded, how would you organize those features into a package?
# 
# There are three separate types of action the package will be doing: first, fetching a page and parsing the HTML for image URL's; second, fetching the images; and third, resizing them. Because of this, you might consider having 3 modules to keep things separate:
# 
# ```
# picture_fetch/
#     __init__.py
#     find.py
#     fetch.py
#     resize.py
# ```
# 

# ### LAB: CREATE A PACKAGE
# In chapter 15 we added error handling to the text cleaning and word frequency counting module we created in chapter 11. Refactor that code into a package containing one module for the cleaning functions, one for the processing functions, and one for the custom exceptions. Then write a simple main function that uses all three.
# 
# ```
# word_count
#     __init__.py
#     exceptions.py
#     cleaning.py
#     counter.py
# ```

# In[ ]:


#__init__.py
from exceptions import EmptyStringError
from cleaning import clean_line, get_words
from counter import count_words, word_stats


# In[ ]:


# exceptions.py
class EmptyStringError(Exception):
    pass


# In[213]:


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
print("\nLeast common words:")
for word in least:
    print(word)


# In[3]:


import word_count
dir(word_count)


# ## Chapter 20

# ### QUICK CHECK : CONSIDER THE CHOICES
# Take a moment to consider what our options are for handling the tasks we’ve identified above. What modules in the standard library can you think of that will do the job? If you want, you can even stop right now and work out the code to do it and compare your solution with the one we’ll develop below.
# 
# From the standard library, `datetime` for managing the dates/times of the files, and either `os.path` and `os` or `pathlib` for renaming and archiving the files.

# ### QUICK CHECK: POTENTIAL PROBLEMS
# Since our solution above is very simple there are likely to be many situations that it won’t handle well. What are some potential issues or problems that might arise with the script above? How might you remedy these problems?
# 
# Multiple files during the same day would be a problem, for one thing. If there are lots of files, it will become increasingly difficult to navigate the archive directory.
# 
# 
# Consider the naming convention used for the files, which is based on the year, month and name, in that order. What advantages do you see in that? What might be the disadvantages? Can you make any arguments for putting the date string somewhere else in the file name, like the beginning or the very end?
# 
# Using year-month-day date formats will make a text based sort of the files sort by date as well. Putting the date at the end of the file name, but before the extension will make it more difficult to parse the date element visually.
# 

# ### TRY THIS: IMPLEMENTATION OF MULTIPLE DIRECTORIES
# Using the code we developed above as a starting point, how would you modify it to implement archiving each set of files in subdirectories named according to the date received? Feel free to take the time to implement the code and test it.

# In[8]:


import datetime
import pathlib

FILE_PATTERN = "*.txt"
ARCHIVE = "archive"

if __name__ == '__main__':
    
    date_string = datetime.date.today().strftime("%Y-%m-%d")

    cur_path = pathlib.Path(".")

    new_path = cur_path.joinpath(ARCHIVE, date_string)
    new_path.mkdir()                                    #A

    paths = cur_path.glob(FILE_PATTERN)

    for path in paths:
        path.rename(new_path.joinpath(path.name))


# ### QUICK CHECK: ALTERNATE SOLUTIONS
# How might you create a script that does the same thing, without using pathlib? What libraries and functions would you use?
# 
# You would use the `os.path` and `os` libraries.

# ### TRY THIS: ARCHIVING TO ZIP FILES PSEUDOCODE
# Take a moment to write the pseudocode for a solution that would store data files in zip files as shown above. What modules and functions or methods do you intend to use? Try coding your solution to make sure it works.
# 
# Pseudocode:
# 
# ```
# create path for zip file
# create empty zipfile
# for each file
#     write into zipfile
#     remove original file
# ```
# 
# (see following text)

# In[ ]:


import datetime
import pathlib
import zipfile

FILE_PATTERN = "*.txt"
ARCHIVE = "archive"

if __name__ == '__main__':
    
    date_string = datetime.date.today().strftime("%Y-%m-%d")

    cur_path = pathlib.Path(".")
    paths = cur_path.glob(FILE_PATTERN)

    zip_file_path = cur_path.joinpath(ARCHIVE, date_string + ".zip")
    zip_file = zipfile.ZipFile(str(zip_file_path), "w")

    for path in paths:
        zip_file.write(str(path))
        path.unlink()


# ### QUICK CHECK: CONSIDER DIFFERENT PARAMETERS
# Take some time to consider different grooming options. How would you modify this to keep only one file a month? How would you change it so that files from the previous month and older were groomed to save one a week? (Note: this is not the same as older than 30 days!)
# 
# You could use something similar to the code above but also check the month of the file against the current month.

# ## Chapter 21

# ### QUICK CHECK: NORMALIZATION
# Look closely at the list of words that was generated above. Do you see any issues with the normalization so far? What other issues do you think you might encounter with a longer section of text? How do you think you might deal those issues?
# 
# Double hyphens for em-dashes, hyphenation for line breaks and otherwise, other punctuation would all be potential problems. 
# 
# Enhancing the word cleaning module created in chapter 18 would be a good way to cover most of the issues.

# ### TRY THIS: READ A FILE
# Write the code to read a text file (assume it’s the file temp_data_00a.txt as show in the the example above) and split each line of the file into a list of values, and add that list to a single list of records. 
# 
# (no answer)

# What issues or problems did you encounter in implementing this? How might you go about converting the last three fields into the correct date, real, and int types?
# 
# You could use a list comprehension and explicitly convert those fields.

# ### QUICK CHECK: HANDLING QUOTING
# Consider how you would approach the problems of handling quoted fields and embedded delimiter characters if you didn't have the `csv` library. Which is easier to handle, the quoting or the embedded delimiters?
# 
# Without using the `csv` module you would have to check to see if a field began and ended with the quote characters, and then strip() them off. 
# 
# To handle embedded delimiters without using the `csv` library, you would have to determine quoted fields and treat them differently, then split the rest of the fields o the delimiter.

# ### TRY THIS: CLEANING DATA
# How would you handle the fields with “Missing” as possible values for math calculations? Can you write a snippet of code that would average one of those columns?
# 
# ```
# clean_field = [float(x[13]) for x in data_rows if x[13] != 'Missing']
# average = sum(clean_field)/len(clean_field)
# ```
# 
# What would you do with the average column at the end, so that you could also report the average coverage? In your opinion would the solution to this problem be at all linked to the way that the “Missing” entries were handled?
# 
# ```
# coverage_values = [float(x[-1].strip("%"))/100]
# ```
# 
# It might or might not be done at the same time as the "Missing" values are handled. 

# ### LAB
# The file of weather observations provided here is by month and then by county for the state of Illinois from 1979 to 2011. Write the code to process this file extract the data for Chicago (Cook County) into a single CSV  or spreadsheet file. This will include replacing the “Missing” strings with empty strings, and translating the percentage to a decimal. You may also consider what fields are repetitive and can be either omitted or stored elsewhere. The proof that you’ve got it right will be in loading the file into a spreadsheet. You can download a solution with the book’s source code.

# ## Chapter 22

# ### TRY THIS: RETRIEVING A FILE
# If you were working with the data file above and wanted to break each line into separate fields, how might you do that? What other processing would you expect to do? Try writing some code to retrieve this file and calculating the average annual rainfall, or for more of challenge, the average maximum and minimum temperature for each year.

# In[43]:


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


# 
# ### LAB: TRACK CURIOSITY’S WEATHER
# Use the API described above in section 22.2 to gather a weather history of Curiosity’s stay on Mars for a month. Transform the data so that you can load it into a spreadsheet and graph it.  For a version of this project see the book’s source code.

# In[ ]:


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
    



# ## Chapter 23

# ### TRY THIS: CREATING AND MODIFYING TABLES
# Using sqlite3 write the code that creates a database table for the Illinois weather data we loaded from a flat file in section 21.2. Suppose that we had similar data for more states, and wanted to store store more information about the states themselves – how could you modify your database to use a related table to store the state information?

# In[61]:


import sqlite3
conn = sqlite3.connect("datafile.db")

cursor = conn.cursor()

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

# In[67]:


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




# ### TRY THIS: MODIFYING A DATABASE WITH ALEMBIC
# Experiment with creating an alembic upgrade that adds a state table to your database, with columns for id, state name, and abbreviation. Upgrade and downgrade. What other changes would be needed if you were going to use the state table along with the existing data table?
# 
# You would need to create a table or perhaps a field relating states to the other tables, and populate it with state data.

# ### QUICK CHECK : USES OF KEY:VALUE STORES
# What sorts of data and applications would benefit most from a key:value store like Redis? 
# 
# * Quick look up of data
# * Caching

# ### QUICK CHECK: USES OF MONGODB
# Thinking back over the various data samples we’ve seen so far and other types of data in your experience, can you come up with any that you think would be well suited to being stored in a database like MongoDB? Are there others that would clearly not be suited, and if so, why not? 
# 
# Data that comes in large and/or more loosely organized "chunks" is suited to MondoDB. For example the contents of a web page, or document, etc.
# 
# Data with a specific structure is better suited to relational data. The weather data we've seen is a good example.

# ### LAB: CREATE A DATABASE
# Choose one of the datasets we’ve discussed in the past few chapters, and decide which type of database would be best to store that data. Create that database and write the code to load the data into it. Then choose the 2 most common and/or likely types of search criteria and write the code to retrieve both single and multiple matching records.
# 
# (no answer)

# ## Chapter 24

# ### TRY THIS: USING JUPYTER NOTEBOOK
# Enter some code in the notebook and experiment with running it. Check out the Edit, Cell, and Kernel menus to see what options are there. Once you have a little code running, use the Kernel menu to restart the kernel, then repeat your steps,  then use the cell menu to rerun the code in all of the cells.
# 
# (no answer)

# ### TRY THIS: CLEANING DATA WITH AND WITHOUT PANDAS
# Experiment with the operations mentioned above. Once the final column has been converted to a fraction, can you think of a way to convert it back to string with the trailing percent sign?
# 
# ```
# temp[17] = temp[17].mul(100)
# temp[17] = temp[17].astype(str) + '%'
# ```
# 
# For contrast, load the same data into a plain Python list of using the csv module, and apply the same changes using just plain Python.  
# 
# Use list comprehensions. So to convert the last column from a string to a fraction, use something like:
# ```
# data = [x[:-1]+[float(x[-1].strip("%"))*100] for x in data]
# ```

# ### QUICK CHECK: MERGING DATA SETS
# How would you go about actually merging to data sets like the above in Python?
# 
# If you were sure you had exactly the same number of items in each set and that they were in the right order, you could use the `zip()` function. Otherwise, you could create a dictionary with the keys being something common between the two data sets and then append the date by key from both sets.

# ### QUICK CHECK: SELECTING IN PYTHON
# What Python code structure would you use to select only rows meeting certain conditions? 
# 
# Probably a list comprehension:
# ```
# selected = [x for x in old_list if <x meets selection criteria>]
# ```

# ### TRY THIS: GROUPING AND AGGREGATING
# Experiment with pandas and the data above. Can you get the calls and amounts by both team member and month?
# 
# ```
# calls_revenue[['Team member','Month', 'Calls', 'Amount']].groupby(['Team member','Month']).sum())
# ```

# ### TRY THIS: PLOTTING
# Plot a line graph of the monthly average amount per call. 

# In[56]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np

# see text for these
calls = pd.read_csv("sales_calls.csv")
revenue = pd.read_csv("sales_revenue.csv")
calls_revenue = pd.merge(calls, revenue, on=['Territory', 'Month'])
calls_revenue['Call_Amount'] = calls_revenue.Amount/calls_revenue.Calls

# plot
calls_revenue[['Month', 'Call_Amount']].groupby(['Month']).mean().plot()

