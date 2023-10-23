import fileinput
def main():
    for line in fileinput.input():
        if fileinput.isfirstline():
            print("<檔案 {0} 的開頭>".format(fileinput.filename()))
        print(line, end="")
main()
