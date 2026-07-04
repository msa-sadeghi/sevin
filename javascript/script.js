async function getPrice() {
  const url =
    "https://brsapi.ir/Api/Tsetmc/Sample/Api_FreeBourseWebService.json";
  const response = await fetch(url);

  if (!response.ok) {
    console.log("error");
  }
  const data = await response.json();
  console.log(data);
}

getPrice();
