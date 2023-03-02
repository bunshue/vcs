import Tkinter as tk
import random
window = tk.Tk()


def randomNoun():
    nouns = ["cats", "hippos", "cakes"]
    noun = random.choice(nouns)
    return noun


def randomVerb():
    verbs = ["eats", "likes", "hates", "has"]
    verb = random.choice(verbs)
    return verb


def buttonClick():
    name = nameEntry.get()
    verb = randomVerb()
    noun = randomNoun()
    sentence = name + " " + verb + " " + noun
    result.delete(0, tk.END)
    result.insert(0, sentence)

nameLabel = tk.Label(window, text="Name:")
nameEntry = tk.Entry(window)

button = tk.Button(window, text="Generate", command=buttonClick)
result = tk.Entry(window)

nameLabel.pack()
nameEntry.pack()
button.pack()
result.pack()

window.mainloop()