#parsing lines in strings 
try:fhand = open('mbox-short.txt')
except FileNotFoundError:
  print('File does not exist')
  exit()

for line in fhand:
  words = line.split()
  if len(words) == 0 or words[0] != 'From':continue
  print(words[2])
fhand.close()

# Write a function called chop that takes a list and modifies
# it, removing the first and last elements, and returns None. Then write
# a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.

# def chop(lst):
#   del lst[0]
#   del lst[-1]
  
# def middle(lst):
#   return lst[1:-1]

# print(chop([1,2,3,4,5,6]))
# print(middle([1,2,3,4,5,6]))