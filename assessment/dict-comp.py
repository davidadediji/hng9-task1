def dict_comp(stop, step):
    a_dict={}
    num=1
    num_list=[]
    for numbers in range(1, stop+1):
        num_list.append(numbers)
        if len(num_list) == step:
            print(num_list)
            a_dict[f"item{num}"]=num_list
            return a_dict
print(dict_comp(3, 4))

#append a value to a key inside a dictionary sample: new_dict["item #"]=[range of numbers defined by steps]
#each string item should have a sequential increase after lenght of 4 (step4)

#pick a range of 1 to stop but once it gets to a step 4 --- lenght 4 break to another item
