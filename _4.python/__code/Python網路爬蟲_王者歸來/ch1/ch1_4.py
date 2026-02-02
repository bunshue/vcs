# ch1_4.py
import json

players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs',
          }
jsonObj = json.dumps(players, sort_keys=True, indent=4)   
print(jsonObj)




