
fname = input('Enter file name: ')
try:fhand = open(fname, 'r')
except FileNotFoundError:
    print('File does not exist')
    exit()

counts = dict()
total_words = ''
new_list = []
for line in fhand:
    line = line.rstrip()
    word = line.split()
    if len(word) == 0 or word[0] != 'From':
        continue
    new_word = word[2] + " "
    total_words += new_word
word_split = total_words.split()
for i in word_split:
    if i not in counts:
        counts[i] = 1
    else:
        counts[i] += 1
lst = list()
for key, value in counts.items():
    lst.append((value, key))
    lst.sort(reverse=False)
print(lst)

    

        

    