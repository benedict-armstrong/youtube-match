from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from get_auth import get_authenticated_service
from test import retrieve_youtube_subscriptions


app = FastAPI(
    title="AE API", openapi_url=f"/openapi.json"
)


@app.get(f"/healthcheck", tags=["healthcheck"])
def healthcheck() -> str:
    return "OK"

@app.get(f"/channels")
def auth() -> str:
    return retrieve_youtube_subscriptions()


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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
