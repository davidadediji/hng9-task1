try:fhand = open('mbox-short.txt', 'r')
except FileNotFoundError:
    print('File does not exist')
    exit()

count = dict()
total_words = ""
for line in fhand:
    line = line.rstrip()
    word = line.split()
    if len(word) == 0 or word[0] != 'From':continue
    sender_email = word[1]
    total_words += sender_email + " "
    
for i in total_words.split():
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

max_no = 0
for s in count:
    if count[s] > max_no:
        max_no = count[s]
for key, value in count.items():
    if max_no == value:
        print(key, value)
            
        

    