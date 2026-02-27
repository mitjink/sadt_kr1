from pydantic import BaseModel, field_validator, Field

# Задание 1.3
class Nums(BaseModel):
    num1: int
    num2: int

class Results(BaseModel):
    result: int

# Задание 1.4
from pydantic import BaseModel

class User(BaseModel):
    name: str
    id: int

# Задание 1.5
from pydantic import BaseModel

class User(BaseModel):
    name: str
    id: int

class User2(BaseModel):
    name: str
    age: int

class User2_Response(BaseModel):
    name: str
    age: int
    is_adult: bool

# Задание 2.1
class Feedback(BaseModel):
    name: str 
    message: str 


# Задание 2.2
class Feedback(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    message: str = Field(min_length=10, max_length=500)

    @field_validator("message")
    def validate_message(cls, text: str):
        bad_words = ["кринж", "рофл", "вайб"]
        text = text.lower()
        for word in bad_words:
            if word in text:
                raise ValueError("Использование недопустимых слов")
        return text
