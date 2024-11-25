from typing import List, Dict, Optional
import yaml
from pydantic import BaseModel


class Resume(BaseModel):
    personal_information: Dict
    work_preferences: Dict
    education_details: Optional[List] = None
    experience_details: Optional[List] = None
    projects: Optional[List] = None
    achievements: Optional[List] = None
    certifications: Optional[List] = None
    languages: List
    interests: Optional[List[str]] = None
    skills: List

    def __init__(self, data: dict):
        try:
            super().__init__(**data)
        except Exception as e:
            raise Exception(f"Неизвестная ошибка во время загрузки данных: {e}") from e
