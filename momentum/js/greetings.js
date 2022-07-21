const loginInput =  document.querySelector("#login-form input");
const loginForm =  document.querySelector("#login-form");
const link = document.querySelector("a");
const greeting = document.querySelector("#greeting");
const HIDDEN_CLASSNAME = "hidden"
const USERNAME_KEY = "username"

function onLoginSubmit(event) {
    event.preventDefault();
    loginForm.classList.add(HIDDEN_CLASSNAME)
    const username = loginInput.value;
    localStorage.setItem(USERNAME_KEY, username)
    paintGreeting(username)
}
function paintGreeting(username) {
    greeting.innerText = `Hi ${username}`
    greeting.classList.remove(HIDDEN_CLASSNAME)
}

const savedUsername = localStorage.getItem(USERNAME_KEY)
console.log(savedUsername);

if (savedUsername === null) {
		// savedUsername이 null이면 form 보이게
    loginForm.classList.remove(HIDDEN_CLASSNAME)
    loginForm.addEventListener("submit", onLoginSubmit);    
} else {
		// savedUsername이 있으면, h1이 나타나도록!
    paintGreeting(savedUsername)  
}