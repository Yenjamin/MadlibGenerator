from tkinter import *

def emptyCheck(var, string):
    while var == "":
        var = input(string)
        var = var.strip()
    return var

def madlib1():
    animals = ""
    animals = emptyCheck(animals, "enter an animal name : ")
    profession = ""
    profession = emptyCheck(profession, "enter a profession : ")
    cloth = ""
    cloth = emptyCheck(cloth, "enter a type of clothing : ")
    things = ""
    things = emptyCheck(things, "enter a noun : ")
    name = ""
    name = emptyCheck(name, "enter the name of a person : ")
    place = ""
    place = emptyCheck(place, "enter the name of a place : ")
    verb = ""
    verb = emptyCheck(verb, "enter a verb in ing form : ")
    food = ""
    food = emptyCheck(food, "enter the name of food : ")
    print('say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' + place +' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as ' + animals + ' pretending to be a ' + profession + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')

def madlib2():
    adjective = ""
    adjective = emptyCheck(adjective, "enter an adjective : ")
    colour = ""
    colour = emptyCheck(colour, "enter a colour : ")
    thing = ""
    thing = emptyCheck(thing, "enter a noun : ")
    place = ""
    place = emptyCheck(place, "enter the name of a place : ")
    person = ""
    person = emptyCheck(person, "enter the name of a person : ")
    adjective1 = ""
    adjective1 = emptyCheck(adjective1, "enter another adjective : ")
    insect = ""
    insect = emptyCheck(insect, "enter the name of an insect : ")
    food = ""
    food = emptyCheck(food, "enter the name of food : ")
    verb = ""
    verb = emptyCheck(verb, "enter a verb : ")
    print('Last night I dreamed I was a ' +adjective+ ' butterfly with ' + colour+ ' splocthes that looked like '+thing+ ' .I flew to ' + place+ ' with my bestfriend and '+person+ ' who was a '+adjective1+ ' ' +insect +' .We ate some ' +food+ ' when we got there and then decided to '+verb+ ' and the dream ended when I said-- lets ' +verb+ '.')

def madlib3():
    person = ""
    person = emptyCheck(person, "enter the name of a person : ")
    colour = ""
    colour = emptyCheck(colour, "enter a colour : ")
    foods = ""
    foods = emptyCheck(foods, "enter the name of food : ")
    adjective = ""
    adjective = emptyCheck(adjective, "enter an adjective : ")
    thing = ""
    thing = emptyCheck(thing, "enter a noun : ")
    place = ""
    place = emptyCheck(place, "enter the name of a place : ")
    verb = ""
    verb = emptyCheck(verb, "enter a verb : ")
    adverb = ""
    adverb = emptyCheck(adverb, "enter an adverb : ")
    food = ""
    food = emptyCheck(food, "enter the name of another food : ")
    things = ""
    things = emptyCheck(things, "enter another noun : ")
    print('Today we picked apple from '+person+ "'s Orchard. I had no idea there were so many different varieties of apples. I ate " +colour+ ' apples straight off the tree that tested like '+foods+ '. Then there was a '+adjective+ ' apple that looked like a ' + thing + '.When our bag were full, we went on a free hay ride to '+place+ ' and back. It ended at a hay pile where we got to ' +verb+ ' ' +adverb+ '. I can hardly wait to get home and cook with the apples. We are going to make appple '+food+ ' and '+things+' pies!.')

display = Tk()
display.geometry("300x300")
display.title("Mad Libs")
Label(display, text="Mad Libs Generator", font="arial 20 bold").pack()
Label(display, text="Choose one :", font="arial 15 bold").place(x=40, y=80)
Button(display, text="The Photographer", font="arial 15", command=madlib1, bg="ghost white").place(x=60, y=120)
Button(display, text="apple and apple", font="arial 15", command=madlib2, bg="ghost white").place(x=70, y=180)
Button(display, text="The Butterfly", font="arial 15", command=madlib3, bg="ghost white").place(x=80, y=240)
display.mainloop()