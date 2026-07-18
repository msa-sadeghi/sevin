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

function getPageData() {
  for (let i = 0; i < SizeCount; i++) {
    const cardElement = document.createElement("div");
    const h3 = document.createElement("h3");
    h3.classList.add("title");
    h3.innerText = data[i]["l30"];
    cardElement.append(h3);
    rootElement.append(cardElement);
  }
}

const rootElement = document.getElementById("root");
const SizeCount = 10;
let pageCount;
async function getPrice() {
  const url =
    "https://brsapi.ir/Api/Tsetmc/Sample/Api_FreeBourseWebService.json";
  const loadingSpan = document.createElement("span");
  loadingSpan.innerText = "در حال بارگذاری ...";
  loadingDiv = document.createElement("div");
  loadingDiv.classList.add("loading");
  rootElement.append(loadingDiv);
  try {
    const response = await fetch(url);
    if (!response.ok) {
      loadingSpan.innerText = "  خطای سرور ...";
      rootElement.append(loadingSpan);
    }
    const data = await response.json();
    pageCount = Math.floor(data.length / SizeCount);
    console.log(pageCount);
    getPageData();

    rootElement.removeChild(loadingDiv);
  } catch (error) {
    loadingSpan.innerText = "خطای سرور   ...";
    rootElement.append(loadingSpan);
  }
}

getPrice();
