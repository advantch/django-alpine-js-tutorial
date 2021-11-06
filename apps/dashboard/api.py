from ninja import Router
from .models import Todo
from .schema import TodoSchema

router = Router()


@router.get("/", operation_id="getTodos")
def list_todos(request):
    return Todo.objects.to_list()


@router.get("/{todo_id}", operation_id="getTodo")
def todo_details(request, todo_id: int):
    todo = Todo.objects.get(id=todo_id)
    return todo.to_json()


@router.delete("/{todo_id}", operation_id="deleteTodo")
def delete_todo(request, todo_id: int):
    return Todo.objects.to_list()


@router.post("/", operation_id="addTodo")
def post_todo(request, payload: TodoSchema):
    return payload
