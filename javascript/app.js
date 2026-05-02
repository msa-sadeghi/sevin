import { products } from "./data.js"
const container = document.querySelector("#product-list")
function renderProducts(){
    container.innerHTML = ""
    products.forEach((p)=>{
        container.innerHTML += `<div class="product-card">
        <img src="${p.image}">
        <h3>${p.title}</h3>
        <p>${p.price}</p>
        <button onclick="addToCard(${p.id})" class="button">Add To Card</button>
        </div>`
    })
}
window.addToCard = addToCard
function addToCard(id){
    let card = JSON.parse(localStorage.getItem("card")) || []
    const item = card.find(p => p.id === id)
    if(item){
        item.qty++
    }else{
        const product = products.find(p=>p.id === id)
        card.push({...product, qty:1})
    }
    localStorage.setItem("card", JSON.stringify(card))
    alert("added")
}
renderProducts()