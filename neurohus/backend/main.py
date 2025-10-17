"""
Neuroljus Neurohus Backend
FastAPI server för Sveriges första digitala hus för empati, kunskap och neurodiversitet
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

# Skapa FastAPI app
app = FastAPI(
    title="Neuroljus Neurohus API",
    description="Sveriges första digitala hus för empati, kunskap och neurodiversitet",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware för frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware för UTF-8 encoding
@app.middleware("http")
async def add_utf8_header(request, call_next):
    response = await call_next(request)
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

@app.get("/")
async def root():
    """
    Välkommen till Neuroljus Neurohus API
    """
    return JSONResponse(
        content={
            "message": "Välkommen till Neuroljus Neurohus",
            "description": "Sveriges första digitala hus för empati, kunskap och neurodiversitet",
            "version": "1.0.0",
            "status": "running"
        },
        headers={"Content-Type": "application/json; charset=utf-8"}
    )

@app.get("/health")
async def health_check():
    """
    Hälsokontroll för API:et
    """
    return JSONResponse(
        content={
            "status": "healthy",
            "message": "Neuroljus Neurohus API är igång och redo att hjälpa"
        },
        headers={"Content-Type": "application/json; charset=utf-8"}
    )

@app.get("/api/verksamheter")
async def get_verksamheter():
    """
    Hämta lista över LSS-verksamheter
    """
    # Mockad data för demo
    return JSONResponse(
        content={
            "verksamheter": [
                {
                    "id": 1,
                    "namn": "Solgården",
                    "kommun": "Stockholm",
                    "typ": "LSS-boende",
                    "betyg": 4.5,
                    "beskrivning": "Ett tryggt och empatiskt boende för personer med autism"
                },
                {
                    "id": 2,
                    "namn": "Vindrosen",
                    "kommun": "Göteborg",
                    "typ": "LSS-boende",
                    "betyg": 4.8,
                    "beskrivning": "Modernt boende med fokus på individuell utveckling"
                }
            ]
        },
        headers={"Content-Type": "application/json; charset=utf-8"}
    )

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )