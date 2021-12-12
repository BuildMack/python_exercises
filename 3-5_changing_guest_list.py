# Exercise 3-5 from Python Crash Course Book
# Completed by Mack Sell

# Importing the previous exercise to add to it:

import importlib

guest_list = importlib.import_module("3-4_guest_list", "3-4_guest_list")


# import fox

# Guest Removal:

noShow = "Paul Dirac"  # Person who will be removed

noShowIndex = fox.guests.index(
    noShow
)  # Need to note the index so we can add a person back to the same spot

fox.guests.remove(
    noShow
)  # Need to use remove() because we did not oriignally know their index

print(f"{noShow} could not make it!")

# Insering new guest to take their place:

fox.guests.insert(noShowIndex, "Chief Sell")

# Printing a message to each guest using the function from the previous exercise:

fox.printList()
