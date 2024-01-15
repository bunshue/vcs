import os
import time
import openpyxl

# User info
firstname = 'David'
lastname = 'Wang'
        
title = 'kkkkkkkk'
age = 22
nationality = 'Taiwan'
            
# Course info
registration_status = 'aaa'
numcourses = 'cccc'
numsemesters = 'ddddd'
            
print("First name: ", firstname, "Last name: ", lastname)
print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
print("# Courses: ", numcourses, "# Semesters: ", numsemesters)
print("Registration status", registration_status)
print("------------------------------------------")

filepath = 'tmp_excel_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.xlsx'
            
if not os.path.exists(filepath):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    heading = ["First Name", "Last Name", "Title", "Age", "Nationality",
               "# Courses", "# Semesters", "Registration status"]
    sheet.append(heading)
    workbook.save(filepath)
workbook = openpyxl.load_workbook(filepath)
sheet = workbook.active
sheet.append([firstname, lastname, title, age, nationality, numcourses,
              numsemesters, registration_status])
workbook.save(filepath)

