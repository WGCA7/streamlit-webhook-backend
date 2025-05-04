from fastapi import FastAPI, Request
import json
import datetime

app = FastAPI()

@app.post("/receive")
async def receive_data(request: Request):
    try:
        # Parse incoming JSON
        data = await request.json()

        # ✅ Log to terminal (Render Logs)
        print("✅ Webhook hit! Incoming data:")
        print(json.dumps(data, indent=4))

        # ✅ Log to separate file for debugging
        timestamp = datetime.datetime.utcnow().isoformat()
        with open("webhook_debug_log.txt", "a") as debug_log:
            debug_log.write(f"\n[{timestamp} UTC] Webhook data:\n")
            debug_log.write(json.dumps(data, indent=4))
            debug_log.write("\n")

        # ✅ Save to file for Streamlit
        with open("latest_webhook_data.json", "w") as f:
            json.dump(data, f, indent=4)

        return {"status": "success", "message": "Data received and saved"}

    except Exception as e:
        error_msg = f"❌ Error in webhook: {str(e)}"
        print(error_msg)
        return {"status": "error", "message": str(e)}


