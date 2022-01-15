#tuples are immutable while lists are mutable, does not support item assignment
#lists are mutable means you can alter the value of an item by its index

# fruits = ['apple', 'orange', 'pineapple']

# fruits[1] = 'mango'
# print(fruits)


# fruit = ('mango', 'orange','guava')
# fruit[1] = 'tamgerine'
# print(fruit)

#Although it is not necessary, it is common to enclose tuples in parentheses to help us quickly identify tuples when we look at Python code:

#covert a string to tuple 
import pandas as pd
a = 'string'
b = tuple(a)
print(type(b))

# convert list to tuple 
fruits = ['mango', 'apple', 'orange']
new_fruits = tuple(fruits)
print(new_fruits)

t = 'a', 'b', 'c'

print(type(t))

b, c = 34, 67
b , c = c, b

print(b, c)

#tuples support indexing and slicing operations , slicing operations doesn't include the stop value
print(t[0])
print(t[:1])

#comparing tuples operators 

print((0, 1, 5) < (0 , 1, 4))

#sort words in a text based on their lenght
txt = 'but soft what light in yonder window breaks'
words = txt.split()

t = list()

for word in words:
    t.append((len(word), word))
print(t)
t.sort(reverse=False)
print(t)

res = list()

for lenght, word in t:
    res.append(word)
print(res)

#seperate a domain and username from a full email address using tuple assignment 

email = 'david.adediji@quabbly.com'

username, domain = email.split('@')
print(username)
print(domain)


# a value error is generated when the number of items assign exceeds the provided variables...

a, b = 1,2 
a, b = b, a



#Dictionaries and Tuples
#dictionaries uses the .items method to print tuples of key, value pairs

empty_dict = {'a':1, 'b': 2, 'd': 3}
# print(empty_dict.items())
#however dictionary items comes in no particular 
word_tuples = list(empty_dict.items())
print(word_tuples)
word_tuples.sort()
print(word_tuples)

#Multiple assignment with dictionaries
lst = list()
for key, val in list(empty_dict.items()):
    lst.append((val, key))
lst.sort(reverse=True)
print(pd.DataFrame(lst))