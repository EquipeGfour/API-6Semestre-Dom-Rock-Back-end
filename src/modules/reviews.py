from db.db import SessionLocal
from models.reviews import Reviews
from models.reviewers import Reviewers
from fastapi import HTTPException
from schemas.schemas import ReviewInput
from sqlalchemy import func
from modules.reviewers import ReviewerController
from models.products import Products
from models.preprocessing_historics import PreprocessingHistorics
from modules.preprocessing_historics import PreprocessingHistoricsController
from sqlalchemy.sql import func
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from db.db import get_db



class ReviewsController:
    def __init__(self) -> None:
        self._preprocessing_controller = PreprocessingHistoricsController()
        self._reviewers_controller = ReviewerController()

    def get_all_reviews(self):
        try:
            db = SessionLocal()
            reviews = db.query(Reviews).all()
            return reviews
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.close()

    def get_review_id(self, review_id: int):
        try:
            db = SessionLocal()
            review = db.query(Reviews).filter(Reviews.id == review_id).first()
            if review is None:
                raise HTTPException(status_code=404, detail="Review not found")
            return review
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.close()

    def insert_review(self, review_input: ReviewInput):
        try:
            db = SessionLocal()
            recommend = self._evaluate_recomend_product(review_input.recomend_product)
            review = Reviews(
                title=review_input.title,
                review=review_input.review,
                rating=review_input.rating,
                recommend_product=recommend
            )
            db.add(review)
            db.commit()      
            db.refresh(review)                              
            return review
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.close()

    def _evaluate_recomend_product(self, recommend:str):
        if recommend.lower() == "yes":
            return True
        else:
            return False
        
    def get_product_rating(self, product_id: int):
        try:
            db = SessionLocal()
            # Calcular a média das avaliações do produto
            count_reviews, avg_rating = db.query(
                func.count(Reviews.product_id),func.avg(Reviews.rating)
                ).join(Products, Reviews.product_id == Products.id).filter(
                    Products.product_id == product_id
                    ).first()
            
            historics = db.query(PreprocessingHistorics
                ).join(Reviews, Reviews.id == PreprocessingHistorics.review_id
                ).join(Products, Reviews.product_id == Products.id
                ).filter(Products.product_id == product_id
                    ).all()
            
            reviews_types = self._preprocessing_controller.count_review_types(historics)
            
            if avg_rating is None:
                avg_rating = 0
            return {"avg_rating": avg_rating, "num_of_reviews": count_reviews, "reviews_types": reviews_types}
        except Exception as e:
            msg = f"[ERROR] - ReviewsController >> Fail to get the product rating, {str(e)}"
            raise HTTPException(status_code = 500, detail = msg)
        finally:
            db.close()
    
    def get_all_reviews_number(self):
        try:
            db = SessionLocal()

            count_all_reviews = db.query(Reviews).count()
            print(count_all_reviews)
            if count_all_reviews == 0:
                msg = f"[ERROR] - ReviewsController >> Reviews not found"
                raise HTTPException(status_code = 404, detail = msg)
            return count_all_reviews
        except Exception as e:
            msg = f"[ERROR] - ReviewsController >> Fail to get the count of reviews into database, {str(e)}"
            raise HTTPException(status_code = 500, detail = msg)
        finally:
            db.close()

    def filter_all_reviewers_by_state(self, state:str):
        try:
            db = SessionLocal()
            reviews = db.query(
                Reviews
                ).join(
                    Reviewers, Reviewers.id == Reviews.reviewer_id, isouter=True
                ).filter(
                    Reviewers.state == state.upper()
                ).all()
            
            historics = db.query(PreprocessingHistorics
            ).join(Reviews, Reviews.id == PreprocessingHistorics.review_id
            ).join(Reviewers, Reviews.reviewer_id == Reviewers.id
            ).filter(Reviewers.state == state.upper()
                ).all()
            
            num_of_reviews = len(reviews)
            formatted_num = 0.0
            rating = 0
            reviews_types = self._preprocessing_controller.count_review_types(historics)
            if num_of_reviews != 0: 
                for review in reviews:
                    rating += review.rating
                formatted_num = "{:.2f}".format(rating/num_of_reviews)          
            response_obj = {
                "num_of_reviews": num_of_reviews,
                "avg_rating": float(formatted_num),
                "reviews_types": reviews_types
            }
            return response_obj
        except Exception as e:
            msg = f"[ERROR] - ReviewsController >> Fail to get the count of reviews by state into database, {str(e)}"
            print(msg)
            raise HTTPException(status_code = 500, detail = msg)
        finally:
            db.close()

    def get_states_and_reviews(self, db: Session = Depends(get_db)):
        top_states = db.query(Reviewers.state, func.count(Reviews.id).label('total_reviews')) \
                    .join(Reviews, Reviewers.id == Reviews.reviewer_id) \
                    .group_by(Reviewers.state) \
                    .order_by(func.count(Reviews.id).desc()) \
                    .all()
        top_states_reviews = [{"state": state, "total_reviews": total_reviews} for state, total_reviews in top_states]
        return top_states_reviews