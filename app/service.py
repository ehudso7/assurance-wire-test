def handler(event):
    return {"ok": True, "event": event.get("id")}
