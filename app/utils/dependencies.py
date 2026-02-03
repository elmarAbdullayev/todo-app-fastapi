from fastapi import HTTPException, status
from app.models import User
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from .security import verify_token
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(db: Session = Depends(get_db),token:str = Depends(oauth2_scheme)) :
    try:
        payload = verify_token(token)
        username:str|None =payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401,detail="Invalid token")
    except:
        raise HTTPException(status_code=401,detail="Invalid token")

    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")

    return user
