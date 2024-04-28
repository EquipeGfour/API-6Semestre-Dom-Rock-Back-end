from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import get_db
from modules.reviewers import ReviewerController
from schemas.schemas import ReviewerInput

router = APIRouter()

@router.post("/insert", description="Route to create a new reviewer")
def create_reviewer(reviewer_data: ReviewerInput, db: Session = Depends(get_db)):
    return ReviewerController().create_reviewer(reviewer_data, db)

@router.get("/all", description="Route to fetch all reviewers")
def get_all_reviewers(db: Session = Depends(get_db)):
    return ReviewerController().get_all_reviewers(db)

@router.get("/get", description="Route to fetch a reviewer by ID")
def get_reviewer_by_id(reviewer_id: int, db: Session = Depends(get_db)):
    reviewer = ReviewerController().get_reviewer_by_id(reviewer_id, db)
    if not reviewer:
        raise HTTPException(status_code=404, detail="Reviewer not found")
    return reviewer


@router.get("/get_top5_statesReviews", description="Route to fetch the top 5 states and their reviews count")
def get_top5_states_reviews(db: Session = Depends(get_db)):
    top_states_reviews = ReviewerController().get_top5_states_by_reviews(db)  # Corrigido o nome do método
    if not top_states_reviews:
        raise HTTPException(status_code=404, detail="Top 5 states not found")
    return top_states_reviews

