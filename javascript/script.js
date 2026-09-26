const rootElement = document.getElementById("root");
window.onload = function viewProfile() {
  const user = JSON.parse(sessionStorage.getItem("user"))[0];
  if (!user) {
    window.location.replace("./login.html");
    return;
  }
  const h1Element = document.createElement("h1");
  const image = document.createElement("img");
  image.style = "width:10%";
  image.src = `${user.image}`;
  h1Element.innerText = `Welcome ${user.username}`;
  h1Element.style = "display:inline-block";

  const logout = document.createElement("a");
  logout.innerText = "logout";
  logout.addEventListener("click", function () {
    sessionStorage.removeItem("user");
    window.location.replace("./login.html");
    
  });

  rootElement.append(image);
  rootElement.append(h1Element);
  rootElement.append(logout);
};
