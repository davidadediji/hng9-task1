# Romeo words 

# fhand = open('romeo.txt', 'r')
# count = dict()
# for line in fhand:
#     line = line.rstrip()
#     words = line.split()
#     for word in words:
#         count[word] = count.get(word, 0) + 1
# print(count)

#advanced text parsing for romeo2.txt with punctuations and spaces

import string

print(string.punctuation)

fname = input('Enter a file name: ')

try:
    fhand = open(fname, 'r')
except FileNotFoundError:
    print('File cannot be opened', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        
max_no = 0
for key, value in list(counts.items()):
    if value > max_no:
        max_no = value

for key, value in list(counts.items()):
    if value == max_no:
        print(key, value)

    