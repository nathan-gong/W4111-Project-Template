from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from uuid import UUID


class NameBasics(BaseModel):
    nconst: str
    primaryName: str
    knownForTitles: str
    primaryProfessions: str
    birthYear: str=None
    deathYear: str=None

    class Config:
        json_schema_extra = {
            "example": {
                "nconst": "nm1234567",
                "John Q. Public"
                "knownForTitles": "tt123456, tt01010101",
                "primaryProfession": "Actor,Director",
                "birthYear": "1900",
                "deathYear": 1999
            }
        }