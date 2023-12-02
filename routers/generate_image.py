from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv
from pathlib import Path
from io import BytesIO
from starlette.responses import StreamingResponse

load_dotenv()

router = APIRouter(
    prefix="/generate-image",
    tags=['Generate image']
)


class ImageRequest(BaseModel):
    prompt: str
    negative_prompt: str | None = None
    height: float | None = None
    width: float | None = None
    num_inference_steps: float | None = None
    guidance_scale: float | None = None
    model: str | None = None


@router.post("/")
async def generate_image(request: ImageRequest):
    client = InferenceClient(token=os.getenv('HUGGINGFACEHUB_API_KEY'))

    try:
        # Generate the image
        image = client.text_to_image(
            prompt=request.prompt,
            negative_prompt=request.negative_prompt,
            height=request.height,
            width=request.width,
            num_inference_steps=request.num_inference_steps,
            guidance_scale=request.guidance_scale,
            model=request.model
        )

        # Save image to a BytesIO object
        img_byte_arr = BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        return StreamingResponse(img_byte_arr, media_type="image/png")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))