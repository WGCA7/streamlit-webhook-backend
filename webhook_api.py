from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.post("/receive")
async def receive_data(request: Request):
    data = await request.json()

    # Save incoming JSON to a file
    with open("latest_webhook_data.json", "w") as f:
        json.dump(data, f, indent=4)

    return {"status": "success", "message": "Data received"}
