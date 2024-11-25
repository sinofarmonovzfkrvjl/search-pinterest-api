from fastapi import FastAPI
from downloader import search_pinterest

app = FastAPI(
    title="Pinterest Search API",
    docs_url="/",
    redoc_url="/docs",
    description="Search for images on Pinterest",
    summary="made by https://t.me/sinofarmonov",
    version="1.0.0",
)

@app.get("/search", tags=["Pinterest Search API"], name="Pinterest Search API", description="search for images on Pinterest")
async def search_images_from_pinterest(keyword: str, limit: int = 10):
    return await search_pinterest(keyword, limit)
