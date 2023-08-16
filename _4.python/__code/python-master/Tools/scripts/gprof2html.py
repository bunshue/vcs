import html
import os
import re
import sys
import webbrowser

header = """\
<html>
<head>
  <title>gprof output (%s)</title>
</head>
<body>
<pre>
"""

trailer = """\
</pre>
</body>
</html>
"""

def add_escapes(filename):
    with open(filename) as fp:
        for line in fp:
            yield html.escape(line)

print('建立html檔案')

filename = 'cccc'

outputfilename = filename + ".html"
input = add_escapes(filename)
output = open(outputfilename, "w")
output.write(header % filename)

output.write(trailer)
output.close()
webbrowser.open("file:" + os.path.abspath(outputfilename))



