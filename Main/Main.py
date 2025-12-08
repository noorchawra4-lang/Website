from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from Database.database import Base, engine
from Models import Models

# ---------------- APP START ----------------

app = FastAPI()

Base.metadata.create_all(bind=engine)

# ---------------- SECURITY ----------------

SECRET_KEY = "mysecret"
ALGO = "HS256"


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


def get_user_by_token(token: str = Depends(oauth2), db=Depends(Models.get_db)):
    error = HTTPException(status_code=401, detail="Invalid token")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGO])
        uid = payload.get("sub")
        if not uid:
            raise error
    except JWTError:
        raise error

    from Models.Models import Register
    user = db.query(Register).filter(Register.id == int(uid)).first()
    if not user:
        raise error

    return user


# ---------------- INCLUDE ROUTERS ----------------

from Routes.Register_routes import router as reg_router
from Routes.Login_routes import router as login_router
from Routes.Category_routes import router as cat_router
from Routes.Manufacture_routes import router as manu_router
from Routes.Order_routes import router as order_router

app.include_router(reg_router)
app.include_router(login_router)
app.include_router(cat_router)
app.include_router(manu_router)
app.include_router(order_router)
