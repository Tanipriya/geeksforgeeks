# siemens interview question


# a= [1, 2, 3,4]

# b= [i*2 for i in a]
# print(b)

# new_dic= {"name": "Tanisha", "city": "Bangalore"}

dict1= {
    "a":5,
    "b":6,
    "c":7,
    "d":8,
    "e": 9
}

dict2= {
    "a":5,
    "b":6,
    "c":7,
    "d":8,
}

new_dict= {}

# new_dict= {}
for k1, v1 in dict1.items():
    
    for k2, v2 in dict2.items():
        
        if  k1== k2:
            new_dict[k1] = v1 +v2
        else :
            new_dict[k1] = k1
print(new_dict)


a= "hello world"
print(a[::-1])

#print max consecutive list

# new_list= [5,3,2,8,7,15,14,12,11, 1, 4, 5, 13, 16,17 ]

# sorted_list=sorted(new_list)
# print(sorted_list)


def max_consecutive_sequence(lst):
    if not lst:
        return []

    # Step 1: Sort the list
    sorted_lst = sorted(lst)
    
    # Initialize variables
    max_seq = []
    current_seq = [sorted_lst[0]]
    print(current_seq)
    
    # Step 2: Iterate through the sorted list
    for i in range(1, len(sorted_lst)):
        if sorted_lst[i] == sorted_lst[i - 1] + 1:
            # If current element is consecutive, add to current sequence
            current_seq.append(sorted_lst[i])
        else:
            # If not consecutive, update max sequence if current is longer
            if len(current_seq) > len(max_seq):
                max_seq = current_seq
            # Start a new sequence
            current_seq = [sorted_lst[i]]
    
    # Check the last sequence
    if len(current_seq) > len(max_seq):
        max_seq = current_seq
    
    return max_seq

new_list = [5, 3, 2, 8, 7, 15, 14, 12, 11, 1, 4, 5, 13, 16, 17]
output = max_consecutive_sequence(new_list)
print(output)


# # o/p = [11, 12,13,14,15,16,17]

list1= []

# for i in new_list:


#print in single array without using flat methods

input1 = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', 'h']

# output = ['a', 'bb', 'ccc', 'ddd', 'ee', 'ff', 'g', 'h']
    
f_list = [value for sub in input1 for value in sub]
print(f_list)


# input1= [1,2,3,[4,5,[6,7]], 9,6]
new= []
for i in input1:
    for j in i:
        for k in j:
            new.append(k)
print(new)
    
