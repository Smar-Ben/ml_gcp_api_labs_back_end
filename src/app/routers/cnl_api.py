from fastapi import APIRouter, status, HTTPException, Query
from services.cnl_api import CloudNaturalLanguageAPIService
from google.api_core.exceptions import InvalidArgument
from typing import List
from models.entity_analysis import EntityAnalysis
from models.classify_analysis import ClassifyAnalysis
from models.sentiment_analysis import SentimentAnalysis


router = APIRouter(
    prefix="/api/cnl",
    tags=["Cloud Natural Language"],
)


@router.get(
    "/entity",
    status_code=status.HTTP_200_OK,
    response_model=List[EntityAnalysis],
    response_description="Fetch Cloud Natural Language API and return the results",
)
async def get_result_cnl_entity(
    text: str | None = Query(default=None, max_length=1000)
):
    """
    get the entity analysis of a text
    :param text: text to analyze
    """
    try:
        return CloudNaturalLanguageAPIService.entity(text)
    except InvalidArgument as e:
        raise HTTPException(status_code=400, detail=str(e)[4:])


@router.get(
    "/sentiment",
    status_code=status.HTTP_200_OK,
    # response_model=SentimentAnalysis,
    response_description="Fetch Cloud Natural Language API and return the results",
)
async def get_result_cnl_entity(
    text: str | None = Query(default=None, max_length=1000)
):
    """
    get the sentiment analysis of a text
    :param text: text to analyze
    """
    try:
        return CloudNaturalLanguageAPIService.sentiment(text)
    except InvalidArgument as e:
        raise HTTPException(status_code=400, detail=str(e)[4:])


@router.get(
    "/classify",
    status_code=status.HTTP_200_OK,
    response_model=List[ClassifyAnalysis],
    response_description="Fetch Cloud Natural Language API and return the results",
)
async def get_result_classify_content(
    text: str | None = Query(default=None, max_length=1000)
):
    """ "
    get content category analysis
    :param text: text to analyze
    """
    try:
        return CloudNaturalLanguageAPIService.classify(text)
    except InvalidArgument as e:
        raise HTTPException(status_code=400, detail=str(e)[4:])
