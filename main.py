from fastapi import FastAPI
from app.features.auth.routers import router as auth_router

app = FastAPI(title="ApnaWaqeel API")

# یہاں ہم تمام فیچرز کے روٹس رجسٹر کرتے ہیں
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

@app.get("/")
def health_check():
    return {"status": "online", "message": "Backend is connected and ready."}