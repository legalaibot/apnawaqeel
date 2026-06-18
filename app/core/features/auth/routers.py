@router.get("/test-connection")
async def test():
    return {"status": "Connected to Python Backend!"}