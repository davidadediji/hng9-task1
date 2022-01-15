# fhand = open('words.txt')
# total_words = ''
# dict_ = dict()

# for line in fhand:
#   line = line.rstrip() + ' '
#   total_words += line
#   lst = total_words.split()
# print(lst)
# keys = dict_.fromkeys(lst, 0)
# print('living' in keys)
# print('all' in keys)
# print('floor' in keys)
# print('break' in keys)
# print('and' in keys)

count1 = 0
count2 = 0
word3 = ''

overall = 'fadeded'
for i in overall:
  if i == 'd':
    count1 += 1
  if i == 'e':
    count2 += 1
print(count1)
print(count2)

word = 'brontosarus'
d = dict()
# for c in word:
#   if c not in d:
#     d[c] = 1
#   else:
#     d[c] += 1
# print(d)


for c in word:
  d[c] = d.get(c, 0) + 1
print(d)