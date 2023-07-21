import sys


print('---- os ------------------------------------------------------------------')	#70個

import os

base_dir = os.path.dirname(os.path.abspath(__file__))

print(base_dir)

import os
user = os.getlogin()
print(user)

font_file = os.path.join(os.path.dirname(__file__), "OpenFlame.ttf")
print(font_file)


print('---- sys ------------------------------------------------------------------')	#70個


print('---- time ------------------------------------------------------------------')	#70個


print('---- print ------------------------------------------------------------------')	#70個

import sys
import os

error = 'mkreal error'

BUFSIZE = 32*1024

sys.stdout = sys.stderr
progname = os.path.basename(sys.argv[0])

print(progname)



print('---- 新進暫存 ------------------------------------------------------------------')	#70個




