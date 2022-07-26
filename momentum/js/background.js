const images = ["0.jpeg", "1.jpeg", "2.jpeg"];

const selectedImages = images[Math.floor(Math.random() * images.length)]

const bgImage = document.createElement("img")
bgImage.src = `img/${selectedImages}`
document.body.appendChild(bgImage);
console.log(bgImage);