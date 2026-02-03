from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse,Token
from app.utils.security import hash_password,verify_password,create_access_token
from app.database import get_db
from app.models import User
from fastapi import HTTPException

router = APIRouter()


@router.post("/register",response_model=UserResponse)
def register(user:UserCreate,db: Session = Depends(get_db)):
    username = db.query(User).filter(User.username == user.username).first()

    if username:
        raise HTTPException(status_code=400,detail="Username already exists")


    if len(user.password) < 6:
        raise HTTPException(status_code=400,detail="Password must be at least 6 characters")


    hashed_password = hash_password(user.password)
    new_user = User(
        username=user.username,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"username":user.username}


@router.post("/login", response_model=Token)
def login(data: UserCreate,db:Session=Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()

    if user is None:
        raise HTTPException(status_code=400,detail="user is not found")

    is_valid  = verify_password(data.password,user.password)

    if is_valid  is False:
        raise HTTPException(status_code=401,detail="Password is false")

    token = create_access_token(data={"sub": user.username})
    print(token)

    return {"access_token": token, "token_type": "bearer"}






