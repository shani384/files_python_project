from fastapi import FastAPI
from .config import settings
from .api.routes import router as api_router

app = FastAPI(title=settings.app_name)

@app.get("/health")
def health():
    return {"status": "ok"}

# מחברים את קבוצת הראוטים של ה-API לאפליקציה
app.include_router(api_router)
