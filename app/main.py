import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.routes.health import router as health_router
from app.core.config import get_settings
from app.core.exceptions import AppException
from app.core.logging import setup_logging

setup_logging()

settings = get_settings()

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.app_name,
    description="AI-powered code investigation and bug patching platform.",
    version="0.1.0",
    debug=settings.debug,
)


@app.exception_handler(AppException)
async def handle_app_exception(
    request: Request,
    exc: AppException,
):
    logger.warning(
        "Application error: %s | Path: %s",
        exc.message,
        request.url.path,
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.message,
            "details": exc.details,
        },
    )


@app.exception_handler(Exception)
async def handle_unexpected_exception(
    request: Request,
    exc: Exception,
):
    logger.exception(
        "Unexpected error | Path: %s",
        request.url.path,
    )

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
        },
    )


app.include_router(health_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
