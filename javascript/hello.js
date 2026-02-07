let firstName = "ali"
let lastName = "ahmadi"

let message1 = `Hello ${firstName} ${lastName}`
console.log(message1)
let message2 = "Hello " + firstName + " " + lastName
console.log(message2)

// let x = Number(prompt("enter a number"))
// let y = Number(prompt("enter a number"))

// console.log(x + y)

let firstNameElement = document.getElementById("firstName")
let lastNameElement = document.getElementById("lastName")
let greet = document.getElementById("greet")

function my(){
    let firstName = firstNameElement.value
    let lastName = lastNameElement.value
    greet.innerHTML = `Hello ${firstName} ${lastName}`
}