from fastapi import APIRouter, HTTPException


router = APIRouter(
    tags=["system"],
    prefix="/api/system",
    dependencies=[],
)


@router.get("/health")
async def health_check():
  """ Health check endpoint """
  logger.info("Health check endpoint")
  return {"status": "ok"}
