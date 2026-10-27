from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class RunRequest(BaseModel):
    question: str


class Vote(BaseModel):
    question_id: str


@router.post("/runs")
async def commission_run(req: RunRequest):
    # Week 1: compute-cap check, dataset fetch (GEO, GTEx, lifespan intervention studies), analysis notebook
    raise HTTPException(status_code=501, detail="private runs not built yet")


@router.get("/questions/current")
async def current_question():
    raise HTTPException(status_code=501, detail="question queue not built yet")


@router.post("/questions/vote")
async def vote(v: Vote):
    raise HTTPException(status_code=501, detail="voting not built yet")


@router.get("/findings")
async def findings():
    raise HTTPException(status_code=501, detail="findings feed not built yet")
