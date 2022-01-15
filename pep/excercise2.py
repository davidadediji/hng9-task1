# Exercise 1: Write a program to read through a file and print the contents
# of the file (line by line) all in upper case.
fname = input('Enter a file name: ')
fhand = open(fname)
count = 0
for line in fhand:
  line = line.rstrip()
  
  if line.startswith('X-DSPAM-Confidence'):
    count += 1
    a = line.find(':')
    print('Average spam confidence:', line[a+1:])
print(count)