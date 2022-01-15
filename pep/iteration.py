# # x = 0
# # x = x + 1
# # print(x)

# #the while statement 

# n = 5

# while n > 0:
#   print('Blastoff')
#   n -= 1

# #using the break statement 
# while True:
#   line = input('> ')
#   if line.lower() == 'done':
#     break
#   print(line)
# print('Done')

# #finishing iterations with the continue statement
# while True:
#   line = input('> ')
#   if line[0] == '#':
#     continue
#   print(line)
#   if line == 'done':
#     break
# print('Done')

#definite loops using for 

friends = ['Joseph', 'Glenn', 'Sally']

for friend in friends:
  print('Happy new Year: ', friend)
print('Done!')

#loop patterns

count = 0
sum = 0
for intervar in [3, 41, 12, 9, 74, 15]:
  count = count + 1
  sum += intervar
  average = sum//count
print("Count: ", count)
print("Sum: ", sum)
print("Average: ", average)

#len()  sum()

max = 0
for value in [1, 2, 3]:
  if value > max:
    max = value
print(max)

smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
  if smallest is None or itervar < smallest:
    smallest = itervar
  print('Loop:', itervar, smallest)
print(smallest)

min = None
for value in [1,2,3,4]:
  if min is None or value < min:
    min = value
print(min)
  