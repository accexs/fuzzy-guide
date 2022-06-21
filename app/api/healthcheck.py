from fastapi import APIRouter

router = APIRouter()


@router.get("/healthcheck")
async def is_alive():
    return {"status": "ok"}
