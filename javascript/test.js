const rootElement = document.getElementById("root")


const firstContainer = document.createElement("div")
firstContainer.classList.add('container')

const nameLabel = document.createElement("label")
nameLabel.innerText = "name"
nameLabel.setAttribute("for", "male")

const nameInputElement = document.createElement("input")
nameInputElement.id = "male"
nameInputElement.type = "radio"

firstContainer.append(nameLabel)
firstContainer.append(nameInputElement)


const btn =  document.createElement("button")
btn.textContent = "register"
btn.style = "padding: 10px; color:red; background-color:cyan; width:100%"

rootElement.append(firstContainer, btn)