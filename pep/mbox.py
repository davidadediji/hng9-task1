fhand = open('mbox-short.txt', 'r')
count = 0
new_list = []
for line in fhand:
  line = line.rstrip()
  new_line = line.split()

  if len(new_line) == 0 or new_line[0] != 'From' :continue
  print(new_line[1])
  
  
try:fhand = open('mbox-short.txt', 'r', encoding="UTF-8")
except FileNotFoundError:
  print('File does not exist')
  exit()

for line in fhand:
  words = line.split()
  if len(words) == 0 or words[0] != 'From':continue
  print(words[2])
fhand.close()
