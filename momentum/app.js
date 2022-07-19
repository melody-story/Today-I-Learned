document.title = "Seongjin Page";



// ```
// const 는 상수 즉 변하지 않는 수  값을 업데이트할 수 없음
// let 아래에서 변수의 값을 업데이트 할 수 있다.
// 변수 convetion : SnakeCase
// ```
// alert("Melody");
const a = 5; 
const b = 2; 
let myName = "Melody"; 

myName = "Seongjin"
console.log(a * b)
console.log(a - b)
console.log(a + b)
console.log("hello"+myName)



function plus(a, b) {
    console.log(a + b);
}

plus(5,6);
plus(7,8);
plus(9,10);


const player= {
    name: "Melody",
    sayHello : function(otherPertsonName) {
        console.log("Hello", otherPertsonName);
    }
}

console.log(player.name);
player.sayHello("Seongjin");

// data type
/// null : 비어있음을 지정, undefine : 안에 아무것도 없어서 보여줄게 없음
//python 에서 null은 None과 동일, go에서 null은 nill과 동일

const me = "Melody"
const days = [1,2,3,4,5,6, true, null, undefined, "text", me]

const toBuy = ["potato", "tomato", "melon"]
console.log(toBuy);
toBuy[2] = "Pizza"
console.log(toBuy);
toBuy.push("apple")
console.log(toBuy);




const age = 96;
function calculateKrAge(ageOfForeigner) {
    // console.log(ageOfForeigner)
    return ageOfForeigner + 2;
}
const krAge = calculateKrAge(age);
calculateKrAge(age)
console.log(krAge);

const calulator = {
    plus : function(a, b){
        return a + b
    },
    minus : function(a, b){
        return a - b
    },
    divide : function(a, b){
        return a / b
    },
    power : function(a, b){
        return a ** b
    },
}

const plusResult = calulator.plus(2,5)
plusResult



const old = parseInt(prompt("How old are you?"))
console.log(typeof old)         // string
console.log(old, parseInt(old)) // NaN : not a number


console.log(isNaN(old));

if (isNaN(old)) {
    console.log("Please write a number")
} else {
    console.log("Thank you for writing your age")
}
if (isNaN(old)) {
    console.log("Please write a number")
} else if (old < 18 ) {
    console.log("You are too young")
} else {
    console.log("You can drink")
}


if (isNaN(old) || old < 0) {
    console.log("Please write a real positive number")
} else if (old < 18) {
    console.log("You are too young")
} else if (old >= 18 && old <=50 ) { // && -> and, || -> or
    console.log("You can drink")
} else if (old > 50 && old <=80 ) { // && -> and, || -> or
    console.log("You should excersise ")
} else if (old > 80) { // && -> and, || -> or
    console.log("You can do wharever")
}

///

console.log(null == undefined); // true 
console.log(null === undefined); // false 
const c = 1; 
const d = "1"; 
console.log(a == b); // true 
console.log(a === b); // false 
console.log(true == 1); // true 
console.log(true === 1); // false 
console.log(0 == "0"); // true 
console.log(0 === "0"); // false 
console.log(0 == ""); // true 
console.log(0 === ""); // false 
console.log(NaN == NaN); // false 
console.log(NaN === NaN); // false 
