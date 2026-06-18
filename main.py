from fastapi import FastAPI
from app.features.auth.routers import router as auth_router

app = FastAPI()

# راؤٹر کو رجسٹر کریں
app.include_router(auth_router, prefix="/auth")

@app.get("/")
async def root():
    return {"message": "Server is running"}