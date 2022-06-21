import logging

from fastapi import FastAPI

from app.api import healthcheck, coalesce

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI():
    application = FastAPI()
    application.include_router(healthcheck.router)
    application.include_router(coalesce.router, prefix="/coalesce")

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
