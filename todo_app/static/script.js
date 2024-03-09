// script.js
const todoText = document.getElementById('todo-text');
const todoList = document.getElementById('todo-items');
const addTodoBtn = document.getElementById('add-todo');

addTodoBtn.addEventListener('click', function() {
  const todoValue = todoText.value.trim();

  if (todoValue) {
    // Create a new list item for the todo
    const todoItem = document.createElement('li');
    todoItem.innerHTML = `<span>${todoValue}</span>
                          <button>&times;</button>`;

    // Add click event listener to remove button
    todoItem.querySelector('button').addEventListener('click', function() {
      todoList.removeChild(todoItem);
    });

    // Add the new todo item to the list
    todoList.appendChild(todoItem);

    // Clear the input field
    todoText.value = '';
  }
});
