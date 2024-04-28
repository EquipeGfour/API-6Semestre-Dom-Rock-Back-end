from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from db.db import get_db
from models.reviewers import Reviewers
from schemas.schemas import ReviewerInput
from models.reviews import Reviews
class ReviewerController:
    def create_reviewer(self, reviewer_data: ReviewerInput, db: Session = Depends(get_db)):
        new_reviewer = Reviewers(
            reviewer_id=reviewer_data.reviewer_id,
            birth_year=reviewer_data.birth_year,
            gender=reviewer_data.gender,
            state=reviewer_data.state
        )
        db.add(new_reviewer)
        db.commit()
        db.refresh(new_reviewer)
        return new_reviewer

    def get_all_reviewers(self, db: Session = Depends(get_db)):
        return db.query(Reviewers).all()

    def get_reviewer_by_id(self, reviewer_id: int, db: Session = Depends(get_db)):
        return db.query(Reviewers).filter(Reviewers.id == reviewer_id).first()

    def get_top5_states_by_reviews(self, db: Session = Depends(get_db)):
        top_states = db.query(Reviewers.state, func.count(Reviews.id).label('total_reviews')) \
                    .join(Reviews, Reviewers.id == Reviews.reviewer_id) \
                    .group_by(Reviewers.state) \
                    .order_by(func.count(Reviews.id).desc()) \
                    .limit(5) \
                    .all()
        top_states_reviews = [{"state": state, "total_reviews": total_reviews} for state, total_reviews in top_states]
        return top_states_reviews