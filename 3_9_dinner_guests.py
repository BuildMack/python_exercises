# Exercise 3-9 from Python Crash Course Book
# Completed by Mack Sell

from importlib import import_module

previousExercise = import_module("3_4_guest_list")

guests = previousExercise.guests

print(f'There are {len(guests)} guests in attendance!')