// 1.

const { error } = require("console")

const promisenew= new Promise(function(resolve, reject) {
    setTimeout(function() {
        console.log("asynch task is complete")
    resolve()

    }, 1000)
})


//2.

promisenew.then(function(){
    console.log("promise consumed")
})


new Promise(function(resolve, reject) {
    setTimeout( function(){
        console.log("asynch 2 task is complete")
        resolve()
    }, 1000)
}).then(function() {
    console.log("promise 2 consumed")
})

//3. 

const promise3= new Promise(function(resolve, reject) {
    setTimeout(() => {
        resolve({name: "Tanisha", designation: "Software Developer"})
    }, 1000);
})
promise3.then(function(details){
    console.log(details)
})

// 4.
const promise4 = new Promise(function(resolve, reject) {
    setTimeout(() => {
        const error = false
        if (!error){
            resolve({name: "Tanisha", gender: "Female"})
        }else{
            reject("getting something wrong ")
        }

    }, 1000);
})
promise4.then(function(user){
    // console.log(user)
    return user.name
}).then((user) => {
    console.log(user)
}).catch(function(error){
    console.log(error)
}).finally(()=> {
    console.log("the promise is either reject or resolve")
})

//5

const promise5 = new Promise(function(resolve, reject){
    setTimeout(function(){
        let error= true
        if (!error){
            resolve({Name: "JavaScript", password: "123456" })
        }else{
            reject("JS went wrong")
        }
    }, 1000)
});

async function consumePromise(){
    try{
        const response = await promise5
        console.log(response)
    }catch   (error){
        console.log(error)
    }
    
}
consumePromise()


// fetching data through Asynch and await methods

async function fetchdata(){
try {
    const response = await fetch("https://api.github.com/users/hiteshchaudhary")
    console.log("user", response)

    
} catch (error) {
    console.log("E",error)
}
}
fetchdata()


// fetching data from .then and .catch mmethods 

const response = fetch("https://api.github.com/users/hiteshchaudhary")
.then((response)=> {
    return response
}).then((data) => {
    console.log(data)
}).catch((error)=>{
    console.log("e", error)
})