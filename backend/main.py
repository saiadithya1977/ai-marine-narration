from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from narration_engine import run_narration_pipeline

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EcosystemInput(BaseModel):
    environment: dict
    actors: list


@app.get("/")
def root():
    return {"message": "Marine Ecosystem Narration API Running"}


@app.post("/narrate")
def narrate_ecosystem(data: EcosystemInput):

    result = run_narration_pipeline(data.dict())

    return result