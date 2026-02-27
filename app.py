from fastapi import FastAPI
from fastapi.responses import FileResponse
import models

app = FastAPI()

# Задание 1.1
# Первый вариант сообщения
@app.get("/")
async def root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}

# Второй вариант сообщения
@app.get("/")
async def root():
    return {"message": "Авторелоад действительно работает"}

# Задание 1.2
@app.get("/")
async def root():
    return FileResponse("index.html")

# Задание 1.3
@app.post("/calculate", response_model=models.Results)
async def calculate(nums: models.Nums):
    return {"result": nums.num1 + nums.num2}

# Задание 1.4
current_user = models.User(name="Мария Доськова", id=1)

@app.get("/users")
async def get_user():
    return current_user

# Задание 1.5
current_user = models.User(name="Мария Доськова", id=1)
current_user2 = models.User2(name="Мария Доськова", age=19)

def adult(age: int) -> bool:
    return age >= 18

@app.post("/user", response_model=models.User2_Response)
async def post_user(u: models.User2):
    return models.User2_Response(name=u.name, age=u.age, is_adult=adult(u.age))

# Задание 2.1
@app.post("/feedback")
async def post_feedback(fb: models.Feedback):
    return {"message": f"Feedback received. Thank you, {fb.name}."}

# Задание 2.2
feedback = []
@app.post("/feedback")
async def post_feedback(fb: models.Feedback):
    feedback.append(fb)
    return {
        "message": f"Спасибо, {fb.name}. Ваш отзыв сохранён"
    }