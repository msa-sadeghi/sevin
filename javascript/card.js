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

                >
                <button>Remove</button>
        `
    });
}


loadCard()