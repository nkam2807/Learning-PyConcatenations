import random

go = input("today we will do string concatenation/adding strings together. type y to proceed")
if go == "y":
  print("lets start")
  print("let's build an opening to a story!")
  print("first, we need some information from you")
  print("you are going to fill in the blanks, and at the end you can read our story! :)")
  noun1 = input("Proper noun? ")
  place1 = input("Place? ")
  verb1 = input("present tense verb? ")
  adjective1 = input("adjective? ")
  noun2 = input("noun? ")
  verb2 = input("past tense verb? ")
  keepGoing = input("keep going? type go ")
  if keepGoing == ("go"):
    print("ok")
    place2 = input("place name? ")
    animal = input("animal? ")
    adjective2 = input("adjective? ")
    print("Welcome " + noun1 + ". You have suddenly woken up in " + place1 + ". IN order to escape, start " + verb1 + " in a " + adjective1 + " manner. Or suffer from the hands of a " + noun2 + ". You got here because you " + verb2 + ", which resulted in kicking you out of your hometown and being scorned by the villagers of, " + place2 + ". Beware! A bright red " + animal + " is staring at you! It is extremely " + adjective2 + " and may attack. If you can successfully avoid it, you will be able to escape. Good luck!")
  else:
    print("Welcome " + noun1 + ". You have suddenly woken up in " + place1 + ". IN order to escape, start " + verb1 + " in a " + adjective1 + " manner. Or suffer from the hands of a " + noun2 + ". You got here because you " + verb2 + ", which resulted in kicking you out of your hometown. Good luck surviving..")
