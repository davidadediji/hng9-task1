stop=10
num_list=[]
for numbers in range(1, stop+1):
    num_list.append(numbers)
    if len(num_list) == 4:
        print(num_list)
