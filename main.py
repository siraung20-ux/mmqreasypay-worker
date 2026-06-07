from fastapi import FastAPI
import requests
import os

app = FastAPI()

MMQR_API_KEY = os.getenv("MMQR_API_KEY")

@app.get("/")
def home():
    return {"status": "Pella API Running"}

@app.post("/create-payment")
def create_payment(data: dict):

    amount = int(data.get("amount", 0))

    if amount < 500 or amount > 1000000:
        return {"error": "Invalid amount"}

    # MMQR API CALL (example format)
    res = requests.post(
        "https://developers.myanmyanpay.com/api/create",
        headers={
            "Authorization": f"Bearer {MMQR_API_KEY}"
        },
        json={
            "amount": amount,
            "currency": "MMK"
        }
    )

    return res.json()
