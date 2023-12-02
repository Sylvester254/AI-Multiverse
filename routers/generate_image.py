from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from huggingface_hub import InferenceClient
import os
from io import BytesIO
from starlette.responses import StreamingResponse

router = APIRouter(
    prefix="/generate-image",
    tags=['Text to Image']
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
    client = InferenceClient(model='stabilityai/stable-diffusion-2-1', token=os.getenv('HUGGINGFACEHUB_API_KEY'))

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

        # Create a filename from the first few characters of the text
        safe_filename = "".join(char if char.isalnum() or char == ' ' else '' for char in request.prompt[:100])
        safe_filename = safe_filename.replace(' ', '_')
        filename = f"{safe_filename}.png" if safe_filename else "image.png"

        return StreamingResponse(
            img_byte_arr,
            media_type="image/png",
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
