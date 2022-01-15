fruit = 'banana'
# letter = fruit[1]
# print(letter)

# #transversal through a string in a loop 
# #with while loop

# index = 0
# while index < len(fruit):
#   letter = fruit[index]
#   print(letter)
  
#   index += 1
  
# for char in fruit:
#   print(char)
  
# #print out the letters one out a time from the word "monkey"
# word = 'monkey'
# index = 0 
# while index < len(word):
#   char = word[index]
#   print(char)
#   index += 1
  
# Write a while loop that starts at the last character in the
# string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.

index = -1
while -len(fruit) <= index:
  char = fruit[index]
  print(char)
  index += -1
  
print(len(fruit))

#string slicing
#[start:stop:step] 
#[the operator returns characters from nth to m-th including the first but excluding the last]

_s = 'Monty Python'
print(_s[:5])
print(_s[6:12])

#count the number of time o appears in 'Monty Python'

count = 0
for char in _s:
  if char == 'o':
    count+=1
print(count)

#encapsulate in a function count
def count(word, spc):
  count = 0
  for char in word:
    if char == spc:
      count+=1
  return count

print(count('Monthy Python', 'P'))

#string comparison 



#string methods

print(dir(_s))
# help(str.count)
  
index = _s.find('a')


line = ' David Adediji   '


#parsing strings

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

atpos = data.find('@')
sppos = data.find(' ', atpos)

host = data[atpos + 1:sppos]


#format operator




# while True:
#   line = input('>>> ')
#   if len(line) == 0 or line[0] == '#':
#     continue
#   if line == 'done':
#     break
#   print(line)
# print('Done!')


str = 'X-DSPAM-Confidence:0.8475'


pre = str.find(':')
integer = str[pre+1:]


if __name__ == '__main__':
  s = 'Banana'
  if s == 'banana':
    print('All right, banana')


  if s < 'banana':
    print('Your word,' + s + ', comes before banana.')
  elif s > 'banana':
    print('Your word,' + s + ', comes after banana.')
  else:
    print('All right, bananas.')
    print(integer)
    print('In %d years I have spotted %g %s'%(3, 0.1, 'camels'))
    print(len(fruit))
    print(host)
    print(line.strip())
    print(s.count('a'))
    print(index)
    
