from fastapi import APIRouter, UploadFile, File, HTTPException
from ..domain.services import build_process_command
from ..adapters.back_client import send_to_back  # ← מייבאים את ה-adapter

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    raw = await file.read()

    try:
        cmd = build_process_command(file.filename, raw)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    try:
        response_from_back = await send_to_back(cmd)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"בעיה בתקשורת עם ה-Back: {str(e)}")

    return {
        "received": True,
        "filename": cmd.filename,
        "queued": True,                # עכשיו הוא נשלח ל-Back
        "back_response": response_from_back  # מה שה-Back ענה
    }
