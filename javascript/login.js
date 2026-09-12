const form = document.querySelector("form");
const username_error = document.querySelector("#username_error");
const password_error = document.querySelector("#password_error");
function login(e) {
  e.preventDefault();
  const username = form.username.value;
  const password = form.password.value;
  if (!username) {
    username_error.innerHTML = `<span>نام کاربری نباید خالی باشد</span>`;
  }
  if (!password) {
    password_error.innerHTML = `<span>کلمه عبور نباید خالی باشد</span>`;
  }
  

}
