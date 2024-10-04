'''
Input: John0000Deo0000Bangalore000024
output: {
"first_name": "john",
"last_name": "deo",
"location": "Bangalore",
"age": 24
}
'''

inp=  "John0000Deo0000Bangalore000024"

s= {}
count= 0
new_list= ["firstName", "lastName", "loaction", "age"]

a= inp.split('0000')
for i in a:
    s[new_list[count]] = a[count]
    count =count+1   
print(s)
