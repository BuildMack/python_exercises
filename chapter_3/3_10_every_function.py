# Exercise 3-10 from Python Crash Course Book
# Completed by Mack Sell

#Using all the topics discussed in Chapter 3

bucketList = ['Paris','Budapest','Lake Cuomo']

bucketList.append('Interlaken')

bucketList.insert(len(bucketList)//2, 'Sand Dune Boarding')

print(f'My alphabetically sorted bucket list:\n{sorted(bucketList)}\n')

print(f'My reverse alphabetically sorted bucket list:\n{sorted(bucketList, reverse=True)}\n')

print('Remove Paris:\n')

bucketList.remove('Paris')

print(bucketList,end ='\n\n')

del bucketList[-1]

firstItem = bucketList.pop(0)

print(f'The first iterm in my list {firstItem} was removed {bucketList}.')

print('Added item and reversed order:\n')

bucketList.append('Return to Germany')

bucketList.reverse()

print(bucketList)

bucketList.sort()

print(f'\nPermanently sorted bucket list using sort() method: \n{bucketList}')


