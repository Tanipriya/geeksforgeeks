let arr= [1,2, [3,2,4], [9,1,2,[2,5,6]], 5]
const fin= [].concat.apply([], arr)
const an= [].concat(...arr)
console.log(arr.flat())

let a= parseInt("12sab")
console.log(a)

let b= eval("10*10+2")
console.log(b)
console.log(typeof(b))

console.log(typeof(NaN))


let v= ["a", "be", "c"]

for (let i of v){
    console.log(i)
}

const promise1 = new Promise(resolve => setTimeout(() => resolve(10), 50))
const promise2 = new Promise(resolve => setTimeout(() => resolve(12), 30))

var addTwoPromises = async function(promise1, promise2) {
    const [value1, value2] = await Promise.all([promise1, promise2])
    // console.log("first", await Promise.all([promise1, promise2]))
return (value1+ value2) 

};
addTwoPromises(promise1, promise2)
  .then(console.log);