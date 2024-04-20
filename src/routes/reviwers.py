from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import get_db
from modules.reviwers import ReviwerController
from schemas.schemas import ReviwerInput

router = APIRouter()

@router.post("/insert", description="Route to create a new reviewer")
def create_reviewer(reviewer_data: ReviwerInput, db: Session = Depends(get_db)):
    return ReviwerController().create_reviewer(reviewer_data, db)

@router.get("/all", description="Route to fetch all reviewers")
def get_all_reviewers(db: Session = Depends(get_db)):
    return ReviwerController().get_all_reviewers(db)

@router.get("/get", description="Route to fetch a reviewer by ID")
def get_reviewer_by_id(reviewer_id: int, db: Session = Depends(get_db)):
    reviewer = ReviwerController().get_reviewer_by_id(reviewer_id, db)
    if not reviewer:
        raise HTTPException(status_code=404, detail="Reviewer not found")
    return reviewer
