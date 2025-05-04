from fastapi import FastAPI, Request
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Optional: Enable CORS for frontend (Streamlit) to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_PATH = "latest_webhook_data.json"

from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.post("/receive")
async def receive_data(request: Request):
    data = await request.json()
    matches = data.get("matches", [])  # Expecting Zapier to wrap the client data in a "matches" array
    with open("latest_webhook_data.json", "w") as f:
        json.dump(matches, f, indent=4)
    return {"status": "success", "message": "Data received"}


@app.get("/latest")
async def get_latest_data():
    try:
        with open(DATA_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"error": "No data yet"}
