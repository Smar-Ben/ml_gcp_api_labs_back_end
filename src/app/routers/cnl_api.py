from fastapi import APIRouter, status
from services.cnl_api import CloudNaturalLanguageAPIService

router = APIRouter(
    prefix="/api/cnl",
    tags=["inference"],
)


@router.get(
    "/entity",
    status_code=status.HTTP_200_OK,
    response_description="Fetch Cloud Natural Language API and return the results",
)
async def get_result_cnl_entity(text: str):
    """ "
    get inference object for image name
    """
    return CloudNaturalLanguageAPIService.entity(text)


@router.get(
    "/sentiment",
    status_code=status.HTTP_200_OK,
    response_description="Fetch Cloud Natural Language API and return the results",
)
async def get_result_cnl_entity(text: str):
    """ "
    save object detected for each inference
    :param inference_results: api input.
    """
    return CloudNaturalLanguageAPIService.sentiment(text)
