# Exercise 4-10 from Python Crash Course Book
# Completed by Mack Sell

cubes = [value**3 for value in range(1,11)]

print(f'First 3 values: {cubes[:3]}')

print(f'Last 3 values: {cubes[-3:]}')

middle_index = len(cubes)//2

print(f'Middle 3 values: {cubes[middle_index-1:middle_index+2]}')

print(f'All the values: {cubes}')