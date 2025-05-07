from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.post("/receive")
async def receive_data(request: Request):
    data = await request.json()
    # support both field names
    if "raw_payload" in data:
        try:
            payload = json.loads(data["raw_payload"])
        except json.JSONDecodeError:
            payload = {}
    elif "body" in data:
        try:
            payload = json.loads(data["body"])
        except json.JSONDecodeError:
            payload = {}
    else:
        payload = data

    # Optional: clear out the file first so you never see stale data
    # if os.path.exists("latest_webhook_data.json"):
    #     os.remove("latest_webhook_data.json")

    with open("latest_webhook_data.json", "w") as f:
        json.dump(payload, f, indent=4)

    return {"status": "success", "message": "Data received"}






