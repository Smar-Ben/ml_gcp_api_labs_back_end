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
    response_description="Fetch Cloud Natural Language API and return the results",
)
async def get_speech_to_text(
    text: str | None = Query(default=None, max_length=255)
):
    """
    get the entity analysis of a text
    :param text: text to analyze
    """
    return TextToSpeechAPIService.convert_speech_to_text(text)
    # try:
    #     return CloudNaturalLanguageAPIService.entity(text)
    # except InvalidArgument as e:
    #     raise HTTPException(status_code=400, detail=str(e)[4:])

