const form = document.querySelector("form");
const username_error = document.querySelector("#username_error");
const password_error = document.querySelector("#password_error");

async function getUsers(username, password) {
  const response = await fetch("./users.json");
  const users = await response.json();
  const user = users.filter(
    (u) => u.username === username && u.password === password,
  );
  if (user.length !== 0) {
    console.log("user founded");
    sessionStorage.setItem("user", JSON.stringify(user));
    location.href = "./index.html";
  } else {
    console.log("user not found");
  }
}
function login(e) {
  e.preventDefault();
  const username = form.username.value;
  const password = form.password.value;
  if (!username) {
    username_error.innerHTML = `<span>نام کاربری نباید خالی باشد</span>`;
  }
  if (!password) {
    password_error.innerHTML = `<span>کلمه عبور نباید خالی باشد</span>`;
  } else {
    password_error.innerHTML = "";
  }
  getUsers(username, password);
}
