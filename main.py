from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}


@app.get("/users")
def get_users():
    return {
        "users": [
            {"id": 1, "name": "Ankit"},
            {"id": 2, "name": "Rahul"},
            {"id": 3, "name": "Priya"}
        ]
    }

@app.get("/about")
def about():
    return {
        "app": "FastAPI Example",
        "version": "1.0.0",
        "description": "This is a simple FastAPI application."
    }



@app.get("/homePage")
def homePage():
    return {"message" : "Hello This is Ankit Jaiswal a Python FullStack Developer aand this is my fastapi project"} 

@app.get("/user/{user_id}")
def get_user(user_id:int):
    users = {
        1: {"id": 1, "name": "Ankit"},
        2: {"id": 2, "name": "Rahul"},
        3: {"id": 3, "name": "Priya"}
    }
    user = users.get(user_id)
    if user:
        return user
    else:
        return {"error": "User not found"}