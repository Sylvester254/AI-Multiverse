from fastapi import FastAPI
from routers.chat import router as chat_router
from routers.generate_image import router as image_router

app = FastAPI(
    title="Chatbot",
    version="1.0",
    description="A chatbot API using LangChain"
)

app.include_router(chat_router)
app.include_router(image_router)
