html = 0

infile = ''
outfile = ''

frames = Interval(",".join(sys.argv[3:]))

try:
    # check if outfile contains a placeholder
    outfile % 1
except TypeError:
    file, ext = os.path.splitext(outfile)
    outfile = file + "%03d" + ext

ix = 1

im = Image.open(infile)

if html:
    file, ext = os.path.splitext(outfile)
    html = open(file+".html", "w")
    html.write("<html>\n<body>\n")

while True:

    if frames[ix]:
        im.save(outfile % ix)
        print(outfile % ix)

        if html:
            html.write("<img src='%s'><br>\n" % outfile % ix)

    try:
        im.seek(ix)
    except EOFError:
        break

    ix += 1

if html:
    html.write("</body>\n</html>\n")


