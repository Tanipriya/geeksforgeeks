'''

let a = "13"
// let b = 2

// console.log(a-b)

// console.log(3+2+ "9"+8)

// console.log(3+2+"5")
// console.log(2+"5")


// const ledger1 = [
//     { id: 2, balance: 2000 },
//     { id: 1, balance: 5000 },
//     { id: 4, balance: 3500 },
//   ];
  
//   let new_id= []
// //   function getNames2() {
//      for (let i of ledger1){
//        if (i['balance'] > 2000){
//         console.log(i['balance']) 
//        }
//      }
'''


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
    print(curr)
    print(rev)
  

if curr:
    print("finalcurr", curr)
    rev.append(curr[::-1])
# print("".join(current))
print("".join(rev))

def reverse_words(sentence):
    # Initialize an empty list to hold the reversed parts of the sentence
    reversed_parts = []
    # Initialize an empty string to hold the current word
    current_word = ''
    
    for char in sentence:
        if char in {',', '.'}:
            # Reverse the current word and append to the reversed_parts list
            reversed_parts.append(current_word[::-1])
            # Append the delimiter to the reversed_parts list
            reversed_parts.append(char)
            # Reset the current word
            current_word = ''
        else:
            # Append the character to the current word
            current_word += char
    
    # Append the last reversed word to the reversed_parts list if any
    if current_word:
        reversed_parts.append(current_word[::-1])
    
    # Join the parts to form the final reversed sentence
    return ''.join(reversed_parts)

# Example usage
input1 = "My, name, is. Shahrukh. Khan"
output1 = reverse_words(input1)
print(output1)  # Output: yM, eman, si. hkurhahS. nahK

