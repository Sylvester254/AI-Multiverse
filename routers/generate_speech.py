from io import BytesIO
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from huggingface_hub import InferenceClient
from starlette.responses import StreamingResponse
import os

router = APIRouter(
    prefix="/text-to-speech",
    tags=['Text to Speech']
)


class TextToSpeechRequest(BaseModel):
    text: str
    model: str | None = None


@router.post("/")
async def text_to_speech(request: TextToSpeechRequest):
    client = InferenceClient(model='facebook/fastspeech2-en-200_speaker-cv4',
                             token=os.getenv('HUGGINGFACEHUB_API_KEY'))

    try:
        # Generate the speech
        audio_bytes = client.text_to_speech(
            text=request.text,
            model=request.model
        )

        # Create a filename from the first few characters of the text
        safe_filename = "".join(char if char.isalnum() or char == ' ' else '' for char in request.text[:100])
        safe_filename = safe_filename.replace(' ', '_')
        filename = f"{safe_filename}.mp3" if safe_filename else "speech.mp3"

        return StreamingResponse(
            BytesIO(audio_bytes),
            media_type="audio/mpeg",
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
