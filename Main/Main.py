from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext

from Database.database import Base, engine, get_db


# ----------- APP START -------------

app = FastAPI()

Base.metadata.create_all(bind=engine)


# ----------- SECURITY -------------

SECRET_KEY = "mysecret"
ALGO = "HS256"
TOKEN_TIME = 60 * 24

oauth2 = OAuth2PasswordBearer(tokenUrl="/login")

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(p):
    return pwd_context.hash(p)


def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)


def create_token(data, time=None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (time or timedelta(minutes=TOKEN_TIME))
    to_encode["exp"] = expire
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGO)


# ----------- TOKEN VERIFY -------------

def get_user_by_token(token: str = Depends(oauth2), db=Depends(get_db)):
    wrong = HTTPException(status_code=401, detail="Invalid token")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGO])
        uid = payload.get("sub")
        if not uid:
            raise wrong
    except JWTError:
        raise wrong

   
    from Models.Models import User

    user = db.query(User).filter(User.id == int(uid)).first()
    if not user:
        raise wrong

    return user


# ----------- ROUTES IMPORT -------------

from Routes.Register_routes import router as reg_router
from Routes.Login_routes import router as login_router
from Routes.Category_routes import router as category_router
from Routes.Manufacture_routes import router as manu_router
from Routes.Order_routes import router as order_router
from Routes.Customer_routes import router as customer_router


# ----------- ROUTES ADD -------------

app.include_router(reg_router)
app.include_router(login_router)
app.include_router(category_router)
app.include_router(manu_router)
app.include_router(order_router)
app.include_router(customer_router)
