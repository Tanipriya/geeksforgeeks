# ITC interview question
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


def reverse_words(sentence):
    reversed_parts = []
    current_word = ''
    
    for char in sentence:
        if char in {',', '.'}:
            reversed_parts.append(current_word[::-1])
            reversed_parts.append(char)
            current_word = ''
        else:
            current_word += char
    
    if current_word:
        reversed_parts.append(current_word[::-1])
    
    return ''.join(reversed_parts)

input1 = "My, name, is. Shahrukh. Khan"
output1 = reverse_words(input1)
print(output1)  


#TCS interview question

# reverse string



'''a = "i am tanisha priya"
# reversed_words = ' '.join(a.split()[::-1])
# print(reversed_words)
print(" ".join(a.split()[::-1]))
'''


'''
Input: John0000Deo0000Bangalore000024
output: {
"first_name": "john",
"last_name": "deo",
"location": "Bangalore",
"age": 24
}
'''

#EVEREST interview question

# convert string to dict
 
'''inp=  "John0000Deo0000Bangalore000024"

s= {}
count= 0
new_list= ["firstName", "lastName", "loaction", "age"]

a= inp.split('0000')
for i in a:
    s[new_list[count]] = a[count]
    count =count+1   
print(s)'''


#Convert Key-Value list Dictionary to List of Lists
test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

newList= []

for k,v in  test_dict.items():
    newList.append([k] + v)
print(newList)


name= {"name", "loacation", "age"}
value= {"Tanisha", "Bangalore", 28}

final= dict(zip(name, value))
print(final)

#print only words, remove all symbol from string
a= "tanisha$% you are_# a great!"

new_str= ""
for i in a:
    if ((i >= "A" and  i <= "Z") or (i >= "a" and i<= "z") or (i == " ")):
        new_str = new_str+ i

print(new_str)

#find max repeated  character in string 

s= "inintitnitin"
dict1 = {}

for i in s:
    if i in dict1 :
        dict1[i] += 1
    else:
        dict1[i] = 1
print(dict1)
new_value= max(dict1, key = dict1.get)
print((new_value))

#chcek palindrome

a= "labal"
b= "check any words is palindrome in labal banab"

# if a[::-1] == a:
#     print("palindrome")
# else:
#     print("no palindrome")

store = []

split1= b.split()
for i in split1:
    if i[::-1] == i:
        store.append(i)
    else:
        continue
print(store)

#find Max number in a list 

inp= [24, 54, 125, 28, 250]

maximum= inp[0]

for i in inp:
    if i > maximum:
        maximum = i
print(maximum)

