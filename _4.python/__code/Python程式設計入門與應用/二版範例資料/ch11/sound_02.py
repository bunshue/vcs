#!/usr/bin/python

# This code is supporting material for the book
# Python Programming for Arduino
# by Pratik Desai
# published by PACKT Publishing

from pyfirmata import Arduino
from time import sleep


# This function performs buzzer patterns according to given parameters
def buzzerPattern(pin, recurrence, pattern):
    # Defining patterns by array of time delays
    pattern1 = [0.8, 0.2,0.6, 0.8,0.7,0.5,0.7]
    pattern2 = [0.2, 0.8]
    flag = True

    # Running the loop for given repetition
    for i in range(recurrence):
        if pattern == 1:
            p = pattern1
        elif pattern == 2:
            p = pattern2
        else:
            print ("Please enter valid pattern. 1 or 2.")
            exit

        # Follow pattern p to turn the buzzer on/off for time delay
        for delay in p:
            if flag is True:
                # Buzzer is on
                board.digital[pin].write(1)
                flag = False
                sleep(delay)

            else:
                # Buzzer is off
                board.digital[pin].write(0)
                flag = True
                sleep(delay)

    # Silent buzzer at the end of the pattern repetition
    board.digital[pin].write(0)
    board.exit()


# Setting up the Arduino board
port = 'COM7'
board = Arduino(port)
# Need to give some time to pyFirmata and Arduino to synchronize
sleep(5)

notes = [ 261, 294, 330, 349, 392, 440, 494, 523 ]
# Execute the 'buzzerPattern' function with custom parameters
#buzzerPattern(10, 2, 1)