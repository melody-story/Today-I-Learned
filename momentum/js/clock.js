const clock = document.querySelector("h2#clock")



function getClock() {
    const date = new Date();  
    // lambda x: x
    const hours = String(date.getHours()).padStart(2,"0")
    const minutes = String(date.getMinutes()).padStart(2,"0")
    const seconds = String(date.getSeconds()).padStart(2,"0")

    currentTime = `${hours}:${minutes}:${seconds}`
    clock.innerText = currentTime
} 
getClock() // 1초의 기다림 없이 웹사이트 실행시 바로 시간이 보이도록 하기위함.
setInterval(getClock, 1000)
