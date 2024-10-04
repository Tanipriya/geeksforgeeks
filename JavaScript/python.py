a= (1,2,3)
b= (2,5,4)

#operator methods
combine= a+b
print(combine)


# through constructor methods
combine_tuple= tuple(a) + tuple(b)
print(combine_tuple)

# using list and extend method
x= list(a)
y= list(b)

x.extend(y)
print(tuple(x))

my_set = {1, 2, 3}
my_set.update([4, 5, 6, 7])
print(my_set)

a_list= [1,2,3,4,5]
b_list= [8,6,7,3]


print(5/2)

class Role:
    def __init__(self, name, role):
        self.name= name
        self.role= role


crd2= Role("Tanisha", "Software Developer")
crs1= Role("Abhisek", "Senior Chief Engineer")

print(crs1.role)

#dunder method for define the operator for instances, many types of dunder availble for assign operators to do functionallity like 
# __add__, __gt__, __mult__, like that.
class order:
    def __init__(self, real, img):
        self.real= real
        self.img= img
    
    def shownumber(self ):
        print(self.real, "i +" , self.img, "j")
        


add1= order(2,3)
add1.shownumber()
add2= order(5,8)    


a= [1,2,4,3,2,7]
print(a.pop(1))
print(a)

a= 6
b= 4.816
c= -3
str1 = '{0:.4f} {0:-3d} {2} {1}' .format(a,b,c)
print(str1)


a= 10020970
split_a= str(a)

# print(split_a.replace("0", "1"))

repl= []
for i in  split_a:
    if i == "0":

        repl.append("1")
    else:
        repl.append(i)
# print(repl)
    
str1= ""

for i in repl:
    str1 += i
print(str1) 
       

new = [1,2,1,3,2,9,69]

a= []

for i in new:
    if i not in a:
        a.append(i)
print(a)


#Remove dubplicates
input= "Python is great and Java is also great great python Python"

a= input.split()

alpha= []

for i in a:
    if  i not in alpha:
        alpha.append(i)
print(" ".join(alpha))
#another methods
print(' '.join(dict.fromkeys(a)))