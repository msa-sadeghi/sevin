let data;
const rootElement = document.getElementById("root");
const container = document.createElement("div");
const progressbarinner = document.getElementById("progressbarinner");
const SizeCount = 10;
let pageCount;
let currentPageNumber = 1;
function getPageData() {
  container.innerHTML = "";
  for (
    let i = (currentPageNumber - 1) * SizeCount;
    i < currentPageNumber * SizeCount;
    i++
  ) {
    const cardElement = document.createElement("div");
    const h3 = document.createElement("h3");
    h3.classList.add("title");
    h3.innerText = data[i]["l30"];
    cardElement.append(h3);
    container.append(cardElement);
  }
  progressbarinner.style.width = `${(currentPageNumber / pageCount) * 100}%`;

  rootElement.append(container);
}
async function getPrice() {
  const url =
    "https://brsapi.ir/Api/Tsetmc/Sample/Api_FreeBourseWebService.json";
  const loadingSpan = document.createElement("span");
  loadingSpan.innerText = "در حال بارگذاری ...";
  loadingDiv = document.createElement("div");
  loadingDiv.classList.add("loading");
  container.append(loadingDiv);
  try {
    const response = await fetch(url);
    if (!response.ok) {
      loadingSpan.innerText = "  خطای سرور ...";
      container.append(loadingSpan);
    }
    data = await response.json();
    pageCount = Math.floor(data.length / SizeCount);
    getPageData();

    container.removeChild(loadingDiv);
  } catch (error) {
    loadingSpan.innerText = "خطای سرور   ...";
    container.append(loadingSpan);
  }
}

getPrice();

togglePrevBtn = () => {
  if (currentPageNumber <= 1) {
    currentPageNumber = 1;
    prevButton.disabled = true;
  }
};
toggleNextBtn = () => {
  if (currentPageNumber >= pageCount) {
    nextButton.disabled = true;
    currentPageNumber = pageCount;
  }
};

const btnContainer = document.createElement("div");
btnContainer.classList.add('btnContainer')
const nextButton = document.createElement("button");
nextButton.innerText = "next";
nextButton.addEventListener("click", () => {
  currentPageNumber++;
  toggleNextBtn();
  if (currentPageNumber > 1) prevButton.disabled = false;
  getPageData();
});
btnContainer.append(nextButton);
const prevButton = document.createElement("button");
prevButton.innerText = "prev";
prevButton.addEventListener("click", () => {
  currentPageNumber--;
  if (currentPageNumber < pageCount) nextButton.disabled = false;
  togglePrevBtn(currentPageNumber);
  getPageData();
});
btnContainer.append(prevButton);
rootElement.append(btnContainer);
togglePrevBtn(currentPageNumber);
