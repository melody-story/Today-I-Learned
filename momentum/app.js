const loginInput =  document.querySelector("#login-form input");
const loginForm =  document.querySelector("#login-form");
const link = document.querySelector("a");
const greeting = document.querySelector("#greeting");
const HIDDEN_CLASSNAME = "hidden"

function onLoginSubmit(event) {
    event.preventDefault();
    loginForm.classList.add(HIDDEN_CLASSNAME)
    const username = loginInput.value;
    console.log(username);
    console.dir(greeting)
    localStorage.setItem("username", username)
    // greeting.innerText = "Hi " + username
    greeting.innerText = `Hi ${username}`
    greeting.classList.remove(HIDDEN_CLASSNAME)
}

loginForm.addEventListener("submit", onLoginSubmit);