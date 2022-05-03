from fastapi import FastAPI
import uvicorn
from core.config.settings import settings
from fastapi.middleware.cors import CORSMiddleware
from api.api import api_router



app = FastAPI(
    title="AE API", openapi_url=f"{settings.API_PREFIX}/openapi.json"
)


@app.get("/healthcheck", tags=["healthcheck"])
def healthcheck() -> str:
    return "OK"


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=f"{settings.API_PREFIX}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
