from pydantic.dataclasses import dataclass
from typing import List
from datetime import datetime


@dataclass
class Inferences:
    image: str
    timestamp: datetime = datetime.now()
