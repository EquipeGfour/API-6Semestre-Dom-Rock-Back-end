from fastapi import APIRouter
from modules.reviews import ReviewsController
from schemas.schemas import ReviewInput


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

@router.get("/product_rating/{product_id}", description="Route to get the average rating of a product")
def get_product_rating(product_id: int):
    return ReviewsController().get_product_rating(product_id)