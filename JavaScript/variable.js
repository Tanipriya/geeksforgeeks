// var , let and const is variable

var  message= " hello Tanisha Priya"
console.log(message)
// console.log("check log")

var text;

text= "hello var variable"
console.log(text)


let val;
val= "const variable name"
console.log(val)

let a = "13"
let b = 2

console.log(a-b)

console.log(3+2+ "9"+8)

console.log(3+2+"5")
console.log(2+"5")

let new_arr= new Array(1,2, "arr", 4)

let n= [1,2,3,4]
console.log(Object.getPrototypeOf(n))

const ledger1 = [
    { id: 2, balance: 2000 },
    { id: 1, balance: 5000 },
    { id: 4, balance: 3500 },
  ];
  
  let new_id= []
//   function getNames2() {
     for (let i of ledger1){
       if (i['balance'] > 2000){
        console.log(i['balance']) 
       }
     }
    //  console.log(new_id)
      
   
//   }
//   console.log(getNames2()); 


let newStr = "tanisha"
let rev= ""

for (let i = newStr.length -1; i >=0; i--){
    rev = rev+ newStr[i]
}
console.log(rev)

const dubArr= [1, 2, 3, 2, 4, 4, 5, 5, 1]

let dub= []

for(let i of dubArr){
  if (!(i  in dub)){
    dub.push(i)
  }
  
}
console.log(dub)
let final= dubArr.filter((item, index) => dubArr.indexOf(item) === index)
console.log(final)

console.log("first", [...new Set(dubArr)]) 


//promise
 function newpromise() {
  const createnewpromise= new Promise((res, rej) => {
    setTimeout(() => {
      // if( Math.random() > 1){
      //   res("data received")
      // }
      // else{
      //   rej("error occured")
      // }

        res("hello tanisha darling")
    }, 2000)
  })
  return createnewpromise
 }
 console.log("first")

 newpromise().then(data => {
  console.log(data)
 })
 .catch(err =>  {
  console.log(err)
 })


 //copy methods

let original = { a: 1, b: 2 };
let shallowCopy = { ...original };
console.log(typeof(shallowCopy))
console.log(original)

//object.assign methods
 let shallowCopy1= Object.assign({}, original)
 console.log(shallowCopy1)

 //object.create methods
 let original2 = { a: 1, b: 2 , c:4, d: 5};
let shallowCopy2 = Object.create(Object.getPrototypeOf(original2), Object.getOwnPropertyDescriptors(original2));
console.log(shallowCopy2)
console.log(typeof(shallowCopy2))

let deepCopy = JSON.parse(JSON.stringify(original));
console.log(deepCopy)