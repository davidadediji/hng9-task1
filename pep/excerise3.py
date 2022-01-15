fhand = open('romeo.txt')

count = 0
total_words = ''
new_list = []
for line in fhand:
  line = line.rstrip('\n') + ' '
  total_words += line
lst=total_words.split()
lst.sort()

for n_word in lst: #traversal of list
  if n_word not in new_list:
    new_list.append(n_word)
print(new_list)
