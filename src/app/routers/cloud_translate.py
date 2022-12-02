from fastapi import APIRouter, status, Query
from services.cloud_translate import CloudTranslateAPIRepositories
from fastapi.responses import FileResponse
from utils.enums.TargetLanguage import TargetLanguage
from models.translation_models import TranslationModels

router = APIRouter(
    prefix="/api/cloud_translate",
    tags=["Cloud Translate"],
)


@router.get(
    "/translation",
    status_code=status.HTTP_200_OK,
    response_model=TranslationModels,
    response_description="Fetch Cloud Translate API to translate a text",
)
async def get_speech_to_text(
    target_language: TargetLanguage, text: str = Query(default=None, max_length=1000)
):
    """
    translate_text translate a text into another languages
    :param target_language: language to translate the text
    :param text: text to analyze
    return translated text 
    """
    return CloudTranslateAPIRepositories.translate_text(target_language, text)
