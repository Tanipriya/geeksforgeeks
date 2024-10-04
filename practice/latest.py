# siemens interview question

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
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
# for k1, v1 in dict1.items():
    
#     for k2, v2 in dict2.items():
        
#         if  k1== k2:
#             new_dict[k1] = v1 +v2
#         else :
#             new_dict[k1] = k1
# print(new_dict)


# a= "hello world"
# print(a[::-1])

new_list= [5,3,2,8,7,15,14,12,11, 1, 4, 5, 13, 16,17 ]

sorted_list=sorted(new_list)
print(sorted_list)

# # o/p = [11, 12,13,14,15,16,17]

# list1= []

# for i in new_list:

# input1 = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', 'h']

# # output = ['a', 'bb', 'ccc', 'ddd', 'ee', 'ff', 'g', 'h']
    
# f_list = [value for sub in input1 for value in sub]
# print(f_list)



# for i in input1:
#     for j in i:
#         for k in j:
#             new.append(k)
# print(new)
    

#ITC Interview question

'''
Write a function to reverse words in the sentence.
Delimiters will be either comma or dot only.
For example:
Input: My, name, is. Shahrukh. Khan
Output: yM, eman, si. hkurhahS. nahK
Input: My,name.is Basavaraj
Output: yM,eman.si jaravasaB
'''



a= "My, name, is. Shahrukh. Khan"

rev= []
curr= ""
for i in a:
    if i in  (',' , "."):
        rev.append(curr[::-1])
        rev.append(i)
        # print("current", curr)

        curr = ""
    else:
        curr += i
        # print("aftercurr", curr)
    # print(curr)
    # print(rev)
  

if curr:
    print("finalcurr", curr)
    rev.append(curr[::-1])
# print("".join(current))
print("".join(rev))

# def reverse_words(sentence):
#     # Initialize an empty list to hold the reversed parts of the sentence
#     reversed_parts = []
#     # Initialize an empty string to hold the current word
#     current_word = ''
    
#     for char in sentence:
#         if char in {',', '.'}:
#             # Reverse the current word and append to the reversed_parts list
#             reversed_parts.append(current_word[::-1])
#             # Append the delimiter to the reversed_parts list
#             reversed_parts.append(char)
#             # Reset the current word
#             current_word = ''
#         else:
#             # Append the character to the current word
#             current_word += char
    
#     # Append the last reversed word to the reversed_parts list if any
#     if current_word:
#         reversed_parts.append(current_word[::-1])
    
#     # Join the parts to form the final reversed sentence
#     return ''.join(reversed_parts)

# # Example usage
# input1 = "My, name, is. Shahrukh. Khan"
# output1 = reverse_words(input1)
# print(output1)  # Output: yM, eman, si. hkurhahS. nahK



matrix= [[j for j in range(5)] for i in range(5)]
print(matrix)

dict1= {x: x**2 for x in [1,2,3,4,5] }
print(dict1)

dict2 = {x: x**3 for x in range(10) if x%2 != 0 }
print(dict2)

a= [[2,3,4], [1,2], [4,6,8]]

flatten_matrix= [x for i in a for x in i]
print(flatten_matrix)


stack = [1,2,3,5]
print(stack[-1])