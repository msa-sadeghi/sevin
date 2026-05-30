function loadCard(){
    const card = JSON.parse(localStorage.getItem("card")) || []
    const container = document.querySelector("#card-items")
    let total = 0
    container.innerHTML = ''
    card.forEach(element => {
        total += element.price * element.querySelector
        container.innerHTML += `
            <div class="card-item">
                <img src="${element.image}">
                <h4>${element.title}</h4>
                <small>
                ${element.price.toLocaleString('fa-IR')} تومان 
                </small>
                <input type="number" min="1" 
                value="${element.qty}"
                onchange="updateQty(${element.id}, this.value)"
                >
                <button onclick="removeItem(${element.id})">Remove</button>
        `
    });
}


loadCard()

function updateQty(id, newQty){
    let card = JSON.parse(localStorage.getItem("card")) || []

    card = card.map(item => {
        if(item.id === id){
            item.qty = parseInt(newQty)
        }
        return item
    })

    localStorage.setItem("card", JSON.stringify(card))
    loadCard()
}

function removeItem(id){
    let card = JSON.parse(localStorage.getItem("card"))
    card = card.filter(p => p.id !== id)
    localStorage.setItem("card", JSON.stringify(card))
    loadCard()
}