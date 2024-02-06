
def getSevSegStr(number, minWidth=0):
    """Return a seven-segment display string of number. The returned
    string will be padded with zeros if it is smaller than minWidth."""

    # Convert number to string in case it's an int or float:
    number = str(number).zfill(minWidth)

    rows = ['', '', '']
    for i, numeral in enumerate(number):
        if numeral == '.':  # Render the decimal point.
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue  # Skip the space in between digits.
        elif numeral == '-':  # Render the negative sign:
            rows[0] += '    '
            rows[1] += ' __ '
            rows[2] += '    '
        elif numeral == '0':  # Render the 0.
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif numeral == '1':  # Render the 1.
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '2':  # Render the 2.
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif numeral == '3':  # Render the 3.
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif numeral == '4':  # Render the 4.
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif numeral == '5':  # Render the 5.
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif numeral == '6':  # Render the 6.
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif numeral == '7':  # Render the 7.
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '8':  # Render the 8.
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif numeral == '9':  # Render the 9.
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'

        # Add a space (for the space in between numerals) if this
        # isn't the last numeral and the decimal point isn't next:
        if i != len(number) - 1 and number[i + 1] != '.':
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '

    return '\n'.join(rows)

print('七段顯示器')

for i in range(0, 1000, 167):
    ccc = getSevSegStr(i, 5)
    print(ccc)

