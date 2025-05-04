from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.post("/receive")
async def receive_data(request: Request):
    try:
        # Parse incoming JSON
        data = await request.json()

        # Log data to Render logs
        print("✅ Webhook hit! Incoming data:")
        print(json.dumps(data, indent=4))

        # Save data to file
        with open("latest_webhook_data.json", "w") as f:
            json.dump(data, f, indent=4)

        return {"status": "success", "message": "Data received and saved"}

    except Exception as e:
        print("❌ Error in webhook:", str(e))
        return {"status": "error", "message": str(e)}


