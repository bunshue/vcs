from random import randint

filename = 'C:/_git/vcs/_1.data/______test_files1/quotes.txt'
#filename = 'C:/_git/vcs/_1.data/______test_files1/poetry2.txt'

def get_random_quote():
    start_line  = None
    end_line    = None

    # Open the quote file
    with open(filename) as file:
        line = file.readlines()
        print('total lines = ', str(len(line)))

    # Let's begin with some random line number
    # When '%%' is found, save the line number and break the loop
    for i in range(len(line)-1):
        random_line = (randint(0, len(line)-1))
        print(random_line)
        if "%%" in line[random_line]:
            start_line = random_line
            print('break at start', start_line)
            break

    # Find the closest next '%%' line number
    for i in range(start_line+1, len(line)):
        if "%%" in line[i]:
            end_line = i
            print('break at end', end_line)
            break

    # We don't need the '%%' to be printed
    start_line += 1

    # Join all the text between these two '%%'
    quote = "".join(line[start_line:end_line])

    return quote

mesg = get_random_quote()
print(mesg)
mesg = get_random_quote()
print(mesg)
mesg = get_random_quote()
print(mesg)
