# backend/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class LoginRequest(BaseModel):
    email: str
    password: str


VALID_USER = {"email": "user@example.com", "password": "Password123!"}


@app.post("/login")
def login(data: LoginRequest):
    # If email + password match our valid user, return success
    if data.email == VALID_USER["email"] and data.password == VALID_USER["password"]:
        return {"token": "fake-jwt-token"}

    # Otherwise, return 400 error
    raise HTTPException(status_code=400, detail="Invalid credentials")
