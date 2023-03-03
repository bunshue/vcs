import random
import Tkinter as tk
window = tk.Tk()

maxNo = 10
score = 0
rounds = 0


def buttonClick():
    global score
    global rounds
    try:
        guess = int(guessBox.get())
        if 0 < guess <= maxNo:
            result = random.randrange(1, maxNo)
            if guess == result:
                score = score + 1
            rounds = rounds + 1
        else:
            result = "Entry not valid"
    except:
        result = "Entry not valid"
    resultLabel.config(text=result)
    scoreLabel.config(text=str(score) + "/" + str(rounds))
    guessBox.delete(0, tk.END)

guessLabel = tk.Label(window, text="Enter a number from 0 to " + str(maxNo))
guessBox = tk.Entry(window)
resultLabel = tk.Label(window)
scoreLabel = tk.Label(window)
button = tk.Button(window, text="guess", command=buttonClick)

guessLabel.pack()
guessBox.pack()
resultLabel.pack()
scoreLabel.pack()
button.pack()

window.mainloop()