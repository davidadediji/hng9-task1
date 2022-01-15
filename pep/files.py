#opening a file
fhand = open('mbox.txt')
print(fhand)

#reading a file
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
  count += 1
print('Line count', count)

#if the file size is small you can read the whole file in one string with the read method
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(len(inp))
print(inp[:21])

#searching through a file (count the no of files that start with from)
count = 0
fhand = open('mbox-short.txt')
for line in fhand:
  if line.startswith('From'):
    count += 1
print(count)

#searching through a file (print all lines that start with from)
with open('mbox-short.txt') as f:
  for line in f:
    line = line.rstrip() #remove newline
    if line.startswith('From'):
      print(line)