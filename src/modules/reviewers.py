from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from db.db import SessionLocal, get_db
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
    
    def get_all_reviewers_by_state(self, state:str):
        try:
            db = SessionLocal()
            all_reviewers = db.query(Reviewers).filter(Reviewers.state == state).all()
            if all_reviewers == None or all_reviewers == []:
                return []
            return all_reviewers
        except Exception as e:
            msg = f"[ERROR] - ReviewersController >> Fail to get the reviewers by state into database, {str(e)}"
            raise HTTPException(status_code = 500, detail = msg)
        finally:
            db.close()