from pydantic.dataclasses import dataclass
from typing import Optional
# from typing import List
# from datetime import datetime

@dataclass
class SentimentAnalysis:
    name: str
    score: float
    magnitude: float
    language: str
