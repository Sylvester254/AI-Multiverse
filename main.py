from fastapi import FastAPI
from dotenv import load_dotenv

from routers.chat import router as chat_router
from routers.generate_image import router as image_router
from routers.generate_speech import router as speech_router

app = FastAPI(
    title="AI Multiverse",
    version="1.0",
    description="FastAPI project that integrates various AI models for different functionalities"
)

load_dotenv()

app.include_router(chat_router)
app.include_router(image_router)
app.include_router(speech_router)
