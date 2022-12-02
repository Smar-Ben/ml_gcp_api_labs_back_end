from pydantic.dataclasses import dataclass
from typing import Optional

# from typing import List
# from datetime import datetime


@dataclass
class TranslationModels:
    text: str
    translation: str
    language_detected: str
