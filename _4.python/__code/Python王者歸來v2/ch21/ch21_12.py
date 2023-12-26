# ch21_12.py
from pygal.maps.world import COUNTRIES

for countryCode in sorted(COUNTRIES.keys()):
    print("國家代碼 :", countryCode, "  國家名稱 = ", COUNTRIES[countryCode])

