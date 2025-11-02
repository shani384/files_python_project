# services/front/src/front/adapters/back_client.py
import httpx
from ..domain.services import ProcessFileCommand
from ..config import settings


async def send_to_back(cmd: ProcessFileCommand) -> dict:

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{settings.BACK_URL}/process",
            json={"filename": cmd.filename, "text": cmd.text},
            timeout=10.0
        )
    response.raise_for_status()
    return response.json()
