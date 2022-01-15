# fhand = open('mbox-short.txt')
# for line in fhand:
#   line = line.rstrip()
#   if not line.startswith('From:'):continue
#   print(line)


# fhand = open('mbox-short.txt')
# for line in fhand:
#   line = line.rstrip()
#   if line.find('@uct.ac.za') == -1: continue
#   print(line)
  
from sys import exit
# #letting the user choose the file name
# fname = input('Enter file name: ')
# try:
# 	fhand = open(fname)
# except FileNotFoundError:
#   print('File cannot be opened:', fname)
#   exit()
  
# count = 0
# for line in fhand:
#   if line.startswith('Subject:'):
#     count+=1
# print('There were', count, 'subject lines in', fname)


#writing to a file 
#the first step to writing to a file involves opening with the mode 'w'

fout = open('output.txt', 'a+')
fout.write('Name is David\nand I want to be rich personnel')
fout.writelines('David')
fout.close()
