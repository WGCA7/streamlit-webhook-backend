@app.post("/receive")
async def receive_data(request: Request):
    try:
        data = await request.json()

        # 🔍 DEBUG: print incoming Zapier payload
        print("📩 Incoming Raw Zapier Data:")
        print(json.dumps(data, indent=4))

        # ✅ Unwrap raw_payload if it's there
        if "raw_payload" in data:
            try:
                data = json.loads(data["raw_payload"])  # Must decode string!
            except json.JSONDecodeError:
                return {"status": "error", "message": "Invalid raw_payload"}

        # 💾 Save file for Streamlit
        with open("latest_webhook_data.json", "w") as f:
            json.dump(data, f, indent=4)

        return {"status": "success", "message": "Data received"}

    except Exception as e:
        return {"status": "error", "message": str(e)}




