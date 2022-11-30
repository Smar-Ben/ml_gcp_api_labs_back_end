from fastapi import APIRouter, status,HTTPException, Query
from services.cnl_api import CloudNaturalLanguageAPIService
from google.api_core.exceptions import InvalidArgument


router = APIRouter(
    prefix="/api/cnl",
    tags=["inference"],
)


@router.get(
    "/entity",
    status_code=status.HTTP_200_OK,
    response_description="Fetch Cloud Natural Language API and return the results",
)
async def get_result_cnl_entity(text: str | None = Query(default=None, max_length=1000)):
    """ "
    get inference object for image name
    """
    try:
        return CloudNaturalLanguageAPIService.entity(text)
    except InvalidArgument as e:
        raise HTTPException(status_code=400, detail=str(e)[4:])


@router.get(
    "/sentiment",
    status_code=status.HTTP_200_OK,
    response_description="Fetch Cloud Natural Language API and return the results",
)
async def get_result_cnl_entity(text: str | None = Query(default=None, max_length=1000) ):
    """ "
    save object detected for each inference
    :param inference_results: api input.
    """
    try:
        return CloudNaturalLanguageAPIService.sentiment(text)
    except InvalidArgument as e:
        raise HTTPException(status_code=400, detail=str(e)[4:])



@router.get(
    "/classify",
    status_code=status.HTTP_200_OK,
    response_description="Fetch Cloud Natural Language API and return the results",
)
async def get_result_classify_content(text: str | None = Query(default=None, max_length=1000)):
    """ "
    save object detected for each inference
    :param inference_results: api input.
    """
    try:
        return CloudNaturalLanguageAPIService.classify(text)
    except InvalidArgument as e:
        raise HTTPException(status_code=400, detail=str(e)[4:])
