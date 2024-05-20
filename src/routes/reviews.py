from fastapi import APIRouter
from modules.reviews import ReviewsController
from schemas.schemas import ReviewInput
from fastapi import Depends, HTTPException
from db.db import get_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/insert", description="Rota para inserir uma review")
def create_review(data:ReviewInput):
    return ReviewsController().insert_review(data)

@router.get("/get", description="Rota para buscar uma review por id")
def get_review_by_id(review_id: int):
    return ReviewsController().get_review_id(review_id=review_id)

@router.get("/all", description="Rota para buscar todos as reviews salvas")
def get_all_review():
    return ReviewsController().get_all_reviews()

@router.get("/all-by-product", description="Route to get the average rating of a product")
def get_product_rating(product_id: int):
    return ReviewsController().get_product_rating(product_id)

@router.get("/get-all-reviews", description="Rota para buscar a quantidade de reviews")
def get_all_reviews_count():
    return ReviewsController().get_all_reviews_number()

@router.get("/get-all-reviews-state", description="Rota para buscar a quantidade de reviews por estado")
def reviews_by_state(state:str):
    return ReviewsController().filter_all_reviewers_by_state(state)

@router.get("/get_top5_statesReviews", description="Route to fetch the top 5 states and their reviews count")
def get_top5_states_reviews(db: Session = Depends(get_db)):
    top_states_reviews = ReviewsController().get_top5_states_by_reviews(db)  # Corrigido o nome do método
    if not top_states_reviews:
        raise HTTPException(status_code=404, detail="Top 5 states not found")
    return top_states_reviews