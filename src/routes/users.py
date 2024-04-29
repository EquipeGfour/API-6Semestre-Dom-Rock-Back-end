from fastapi import APIRouter, Depends
from db.db import get_db
from sqlalchemy.orm import Session
from schemas.schemas import UsersInput
from modules.users import UsersController
from schemas.schemas import LoginInput

router = APIRouter()

@router.get("/get", description="Rota para buscar um usuário pelo ID")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return UsersController().get_user(user_id, db)

@router.get("/all", description="Rota para obter todos os usuários")
def get_all_users(db: Session = Depends(get_db)):
    return UsersController().get_all_users(db)

@router.post("/insert", description="Rota para inserir um novo usuário")
def insert_user(user_data: UsersInput, db: Session = Depends(get_db)):
    return UsersController().insert_user(user_data, db)

@router.put("/put", description="Rota para atualizar os dados de um usuário")
def update_user(user_id: int, user_data: UsersInput, db: Session = Depends(get_db)):
    return UsersController().update_user(user_id, user_data, db)

@router.delete("/delete", description="Rota para excluir um usuário pelo ID")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return UsersController().delete_user(user_id, db)

@router.post("/login", description="Rota para fazer login")
def login(user_data: LoginInput, db: Session = Depends(get_db)):
    return UsersController().login(user_data, db)
