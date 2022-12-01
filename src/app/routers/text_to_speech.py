from fastapi import APIRouter, status, HTTPException, Query
from google.api_core.exceptions import InvalidArgument
from services.text_to_speech import TextToSpeechAPIService
from fastapi.responses import FileResponse


router = APIRouter(
    prefix="/api/text_to_speech",
    tags=["Text-to-Speech API"],
)


@router.get(
    "/text_to_speech",
    status_code=status.HTTP_200_OK,
    response_class=FileResponse,
    response_description="Fetch Cloud text_to_speech API to transform a text into speech",
)
async def get_speech_to_text(
    text: str | None = Query(default=None, max_length=255)
):
    """
    transform a speech into a text with text_to_speech api
    :param text: text to analyze
    """
    return TextToSpeechAPIService.convert_speech_to_text(text)