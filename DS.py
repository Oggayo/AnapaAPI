from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# Простая база данных в памяти для хранения балансов пользователей
balances: Dict[str, int] = {}

# Модель запроса для депозита


class DepositRequest(BaseModel):
    user_id: str
    amount: int


@app.post("/deposit")
async def deposit(request: DepositRequest):
    if request.amount <= 0:
        raise HTTPException(status_code=400, detail="Deposit amount must be positive")

    if request.user_id not in balances:
        balances[request.user_id] = 0

    balances[request.user_id] += request.amount

    return {"user_id": request.user_id, "new_balance": balances[request.user_id]}


@app.get("/balance/{user_id}")
async def get_balance(user_id: str):
    if user_id not in balances:
        raise HTTPException(status_code=404, detail="User not found")

    return {"user_id": user_id, "balance": balances[user_id]}


@app.get("/")
async def root():
    return {"message": "Welcome to the Token Deposit API"}


# Запуск приложения
if 'name' == "main":
    uvicorn.run(app, host="0.0.0.0", port=8000)


class DepositRequest(BaseModel):
    user_id: str
    amount: int


class TransferRequest(BaseModel):
    from_user_id: str
    to_user_id: str
    amount: int


@app.post("/deposit")
async def deposit(request: DepositRequest):
    if request.amount <= 0:
        raise HTTPException(status_code=400, detail="Deposit amount must be positive")

    if request.user_id not in balances:
        balances[request.user_id] = 0

    balances[request.user_id] += request.amount

    return {"user_id": request.user_id, "new_balance": balances[request.user_id]}


@app.post("/transfer")
async def transfer(request: TransferRequest):
    if request.amount <= 0:
        raise HTTPException(status_code=400, detail="Transfer amount must be positive")

    if request.from_user_id not in balances or balances[request.from_user_id] < request.amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    if request.to_user_id not in balances:
        balances[request.to_user_id] = 0

    balances[request.from_user_id] -= request.amount
    balances[request.to_user_id] += request.amount

    return {
        "from_user_id": request.from_user_id,
        "to_user_id": request.to_user_id,
        "new_balance_from_user": balances[request.from_user_id],
        "new_balance_to_user": balances[request.to_user_id]
    }


@app.get("/balance/{user_id}")
async def get_balance(user_id: str):
    if user_id not in balances:
        raise HTTPException(status_code=404, detail="User not found")

    return {"user_id": user_id, "balance": balances[user_id]}


@app.get("/")
async def root():
    return {"message": "Welcome to the Token Transfer API"}

if "name" == "main":
    uvicorn.run(app, host="0.0.0.0", port=8000)
