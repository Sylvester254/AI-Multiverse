from fastapi import APIRouter
from langchain.llms import HuggingFaceHub
from pydantic import BaseModel
import os
from langchain.prompts import ChatPromptTemplate
from langchain.chains import ConversationChain

router = APIRouter(
    prefix="/chat",
    tags=['Chat with AI']
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


@router.post("/", response_model=ChatResponse)
async def chat(chat_request: ChatRequest):
    # Define your prompt template and chain
    template = "You are a helpful assistant."
    human_template = chat_request.message

    print(human_template)

    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", template),
        ("human", human_template),
    ])

    load_dotenv()
    repo_id = 'openchat/openchat_3.5'
    llm = HuggingFaceHub(huggingfacehub_api_token=os.getenv('HUGGINGFACEHUB_API_KEY'),
                                         repo_id=repo_id)
    conversation = ConversationChain(llm=llm)
    # conversation.run(chat_prompt)

    response_message = conversation.run(chat_prompt)

    return ChatResponse(reply=response_message)
