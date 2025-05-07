from fastapi import FastAPI, Request
import json
import os

app = FastAPI()  # ✅ This must be BEFORE any route decorators

@app.post("/receive")
async def receive_data(request: Request):
    data = await request.json()
    if "body" in data:
        # body is a JSON‐string of your real payload
        payload = json.loads(data["body"])
    else:
        payload = data

    with open("latest_webhook_data.json", "w") as f:
        json.dump(payload, f, indent=4)

    return {"status": "success", "message": "Data received"}





