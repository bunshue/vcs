# ch34_9.py
from functools import reduce
from PIL import Image
import math, operator
h1 = Image.open("face1.jpg").histogram()
h2 = Image.open("face1.jpg").histogram()
RMS = math.sqrt(reduce(operator.add, list(map(lambda a,b:
                (a-b)**2, h1, h2)))/len(h1))
print("RMS = ", RMS)



