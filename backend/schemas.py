from pydantic import BaseModel
from typing import List, Optional


class Environment(BaseModel):
    type: str
    time_of_day: Optional[str] = None
    temperature_c: Optional[float] = None


class Actor(BaseModel):
    id: str
    species: str
    behaviors: List[str]
    target: Optional[str] = None


class EcosystemData(BaseModel):
    environment: Environment
    actors: List[Actor]