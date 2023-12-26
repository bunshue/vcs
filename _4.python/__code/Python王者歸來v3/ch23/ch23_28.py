# ch23_28.py
import sys, webbrowser

print(sys.argv[0])
if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
webbrowser.open('http://www.google.com.tw/maps/place/' + address)


