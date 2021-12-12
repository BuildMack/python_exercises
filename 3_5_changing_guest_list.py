# Exercise 3-5 from Python Crash Course Book
# Completed by Mack Sell

# Importing the previous exercise to add to it:

# This package can be used when you are dealing with a file that starts with a number:

from importlib import import_module

previousExercise = import_module("3_4_guest_list")

# Alternative Option:
# fox = __import__("3_4_guest_list")

# Guest Removal:

guests = previousExercise.guests

noShow = "Paul Dirac"  # Person who will be removed

noShowIndex = guests.index(noShow)  # Need to note the idndex so we can add a person back to the same spot

guests.remove(noShow)  # Need to use remove() because we did not oriignally know their index

print(f"{noShow} could not make it!")

# Insering new guest to take their place:

guests.insert(noShowIndex, "Chief Sell")

# Printing a message to each guest using the function from the previous exercise:

previousExercise.printList()
