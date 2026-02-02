# ch1_23.py
import xmltodict

with open('myxml.xml', encoding='utf-8') as f:
    txt = xmltodict.parse(f.read())
print(txt,'\n')
print(txt['深智數位'],'\n')
print('總經理 : ',txt['深智數位']['總經理'])
print('總編輯 : ',txt['深智數位']['編輯部'],'\n')
print(txt['深智數位']['業務部'],'\n')
print(txt['深智數位']['業務部']['國外'],'\n')
print('國外業務主管 : ',txt['深智數位']['業務部']['國外']['@主管'])
print('國外業務人數 : ',txt['深智數位']['業務部']['國外']['人數'])
print('國內業務主管 : ',txt['深智數位']['業務部']['國內'])









