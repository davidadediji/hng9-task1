listdictionary = dict()


lst = listdictionary.fromkeys(['d', 'a', 'c'], 0)
print(lst)

#to assign a key-value pair to a dictionary 
empty_dict = {}

empty_dict['one'] = 2 
empty_dict['two'] = 3
print(empty_dict)

#use len function with a dictionary 
print(len(empty_dict))

#To access a value in a dictionary
print(empty_dict['two'])

#the in operator also works in a dictionary 

print('one' in empty_dict)

for num in empty_dict:
    print(empty_dict[num])
    
    
#get values from a dictionary 
new_list = list(empty_dict.values())
print(new_list)

# the .get method in dictionary

print(empty_dict.get('two', 0))

#looping and dictionary 

counts = {'chuck': 1, 'annie': 42, 'jan': 100}
for key in counts:
    print(key, counts[key])

#find entries below 100
for key in counts:
    if counts[key] < 100:
        print(key, counts[key])