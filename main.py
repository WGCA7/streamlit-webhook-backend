from fastapi import FastAPI, Request
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_PATH = "latest_webhook_data.json"

@app.post("/receive")
async def receive_data(request: Request):
    data = await request.json()
    matches = data.get("matches", [])
    with open(DATA_PATH, "w") as f:
        json.dump(matches, f, indent=4)
    return {"status": "success", "message": "Data received"}

@app.get("/latest")
async def get_latest_data():
    try:
        with open(DATA_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"error": "No data yet"}

