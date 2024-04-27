from db.db import SessionLocal
from models.reviews import Reviews
from fastapi import HTTPException
from schemas.schemas import ReviewInput
from sqlalchemy import func


class ReviewsController:
    def get_all_reviews(self):
        db = SessionLocal()
        reviews = db.query(Reviews).all()
        return reviews

    def get_review_id(self, review_id: int):
        db = SessionLocal()
        review = db.query(Reviews).filter(Reviews.id == review_id).first()
        if review is None:
            raise HTTPException(status_code=404, detail="Review not found")
        return review

    def insert_review(self, review_input: ReviewInput):
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

    def _evaluate_recomend_product(self, recommend:str):
        if recommend.lower() == "yes":
            return True
        else:
            return False
        
    def get_product_rating(self, product_id: int):
        db = SessionLocal()

        # Verificar se existem avaliações para o produto em questão
        count_reviews = db.query(Reviews).filter(Reviews.product_id == product_id).count()
        print(count_reviews)
        if count_reviews == 0:
            raise HTTPException(status_code=404, detail="Não existe esse produto")

        # Calcular a média das avaliações do produto
        avg_rating = db.query(func.avg(Reviews.rating)).filter(Reviews.product_id == product_id).scalar()
        db.close()

        if avg_rating is None:
            raise HTTPException(status_code=404, detail="Não há notas para esse produto")
        
        return avg_rating