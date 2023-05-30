url = 'http://www.google.com'
#url = 'https://www.gmail.com'
mail_address = 'XXXXXXX'
password = 'XXXXXXX'

import time
from selenium import webdriver

#driver = webdriver.Firefox();
driver = webdriver.Chrome()

driver.get(url);
#username = driver.find_element_by_id('identifierId');
username = driver.find_element("name", "identifierId")
username.send_keys(mail_address);

driver.find_elements_by_class_name('RveJvd.snByac')[1].click();
time.sleep(2); #password not entered in username field
password = driver.find_element_by_class_name('whsOnd.zHQkBf');

password.send_keys(password);
driver.find_elements_by_class_name('RveJvd.snByac')[0].click();

#end login, start composing

time.sleep(5); #wait for sign in
driver.find_element_by_class_name('T-I.J-J5-Ji.T-I-KE.L3').click();
to = driver.find_element_by_class_name('textarea#:lo.vO'); #incorrect
to.send_keys("EMAIL");
#subject = driver.find_element_by_id(':l6');
subject = driver.find_element("name", ":l6")

subject.send_keys("IP Address changed");
#content = driver.find_element_by_id(':m9');
content = driver.find_element("name", ":m9")

content.send_keys("Test Test\n");


