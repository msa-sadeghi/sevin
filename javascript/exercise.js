const url = "http://127.0.0.1:3000/api/products";
const fetchProducts = async (url) => {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      console.log("server error");

      return [];
    }
    const products = await response.json();
    console.log(products);
  } catch (ex) {
    console.log("error");
    return [];
  }
};

fetchProducts(url);
