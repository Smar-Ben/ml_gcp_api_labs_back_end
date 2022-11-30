from pydantic.dataclasses import dataclass
from typing import Optional
# from typing import List
# from datetime import datetime


@dataclass
class EntityAnalysis:
    name: str
    type: str
    score: float
    language: str
    wikipedia_url:Optional[str]=None 
