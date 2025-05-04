from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.post("/receive")
async def receive_data(request: Request):
    try:
        # Parse incoming JSON from Zapier
        data = await request.json()

        # If using 'raw_payload' (JSON string inside), decode it
        if "raw_payload" in data:
            try:
                data = json.loads(data["raw_payload"])
            except json.JSONDecodeError:
                return {
                    "status": "error",
                    "message": "Failed to parse JSON inside 'raw_payload'."
                }

        # Save to a file for use in Streamlit
        with open("latest_webhook_data.json", "w") as f:
            json.dump(data, f, indent=4)

        return {
            "status": "success",
            "message": "Data received",
            "clients_found": len(data.get("clients", [])) if "clients" in data else 0
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }



