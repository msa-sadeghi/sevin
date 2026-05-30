import { products } from "./data.js"
const container = document.querySelector("#product-list")
const searchInput = document.querySelector('#search')


searchInput.addEventListener('input', ()=>{
    const value = searchInput.value.toLowerCase()
    const filtered = products.filter(p => {
        return p.title.toLowerCase().includes(value)
    })
  
    renderProducts(filtered)
})



function renderProducts(products){
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
renderProducts(products)