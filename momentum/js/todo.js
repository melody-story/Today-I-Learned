const todoFrom = document.getElementById("todo-form");
// const todoInput = document.querySelector('#todo-form input'); 
const todoInput = todoFrom.querySelector('input'); 
const todolist = document.getElementById("todo-list"); 


function deleteToDo(event) {
    /*
        클릭한 곳을 감지해서 해당 부위만 삭제하고 싶은데, button이 너무 많아서 구분이 쉽지않다.
        그럴 때는, eventlistener가 넘겨주는 event에 관한 정보를 이용해보자.
        tartget이라는 속성에 보면, event가 발생한 분에 대한 정보가 나와있는데, 
        특히 parentElement라는 button의 상위 엘레먼트인 li부분을 볼 수 있다. 
        삭제버튼을 누름과 동시에 해당 버튼이 들어있는 li하나가 사라지게끔 해야하므로,
        코드는 아래와 같이 나올 수 가 있겠다. 
    */
    const li = event.target.parentElement;
    li.remove()
    console.log(event.target.parentElement);
    console.log(event.target.parentElement.innerText);
}

function paintToDo(newTodo) {
    const li = document.createElement('li')
    const span = document.createElement('span')
    span.innerText=newTodo
    const button = document.createElement('button')
    button.innerText = "🗑"
    li.appendChild(span)
    li.appendChild(button)
    todolist.appendChild(li)
    // 버튼의 클릭이벤트를 감지함. 
    button.addEventListener('click', deleteToDo)
    
}
function handleToDoSubmit(event) {
    event.preventDefault();
    console.log();
    const newTodo = todoInput.value;
    todoInput.value = ""; // 입력후 엔터를 쳤을 때, 화면에 값이 나타나지 않게 함.
    paintToDo(newTodo);

}

todoFrom.addEventListener('submit',handleToDoSubmit);
// todolist.addEventListener('submit',handleToDoDelete);