from fastapi import FastAPI, HTTPException, status
import uvicorn

app = FastAPI()
tasks = []


@app.get("/")
def home():
    return {"message": "Список задач"}


@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}


@app.post(
    "/tasks",
    responses={
        201: {"description": "Задача создана"}
    },
    status_code=status.HTTP_201_CREATED
)
def add_task(task: str):
    tasks.append(task.strip())
    return {"message": "Добавлено", "task": task.strip()}


@app.delete(
    "/tasks/{index}",
    responses={
        400: {"description": "Неверный индекс"},
        404: {"description": "Задача не найдена"}
    }
)
def delete_task(index: int):
    if index < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Индекс не может быть отрицательным"
        )
    if index >= len(tasks):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Задача с индексом {index} не найдена"
        )
    deleted = tasks.pop(index)
    return {"message": "Удалено", "task": deleted}


uvicorn.run(app)
