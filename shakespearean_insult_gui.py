from random import choice
from guizero import App, Box, Text, PushButton
list_a = []
list_b = []
list_c = []
with open("insults.csv", "r") as f:
    for line in f:
        words = line.split(',')
        list_a.append(words[0])
        list_b.append(words[1])
        list_c.append(words[2])


def insult_me():
    word_a = choice(list_a)
    word_b = choice(list_b)
    word_c = choice(list_c)
    insult = "Thou {} {} {} !".format(word_a, word_b, word_c.rstrip())
    return insult


def new_insult():
    new_insult = insult_me()
    message.value = new_insult


app = App("Shakespearean Insult Generator")

message = Text(app, insult_me())
button = PushButton(app, new_insult, text="Insult Me Again...")
box = Box(app, width=10, height=10)
app.display()
