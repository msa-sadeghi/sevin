// function getPrice() {
//   console.log("start");
//   console.log("end");
// }
// getPrice();

// function delay() {
//   return new Promise((resolve) => {
//     setTimeout(() => resolve("data recieved"), 2000);
//   });
// }

// async function getPrice() {
//   console.log("start");
//   const result = await delay();
//   console.log(result);
//   console.log("end");
// }

const rootElement = document.getElementById("root");

getPrice();
async function getPrice() {
  const url =
    "https://brsapi.ir/Api/Tsetmc/Sample/Api_FreeBourseWebService.json";
  const response = await fetch(url);

  if (!response.ok) {
    console.log("error");
  }
  const data = await response.json();
  for (let i = 0; i < data.length; i++) {
    const cardElement = document.createElement("div");
    const h3 = document.createElement("h3");
    h3.classList.add("title");
    h3.innerText = data[i]["l30"];
    cardElement.append(h3);

    console.log(data[i]);

    rootElement.append(cardElement);
  }
}

getPrice();
