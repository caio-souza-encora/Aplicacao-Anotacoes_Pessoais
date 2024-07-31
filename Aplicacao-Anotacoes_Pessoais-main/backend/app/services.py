from app.models import User
from app.connection import SessionLocal as Session
from datetime import datetime
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def get_password_hash(password: str) -> str:
        return pwd_context.hash(password)

    def create_user(user_input):
        hashed = get_password_hash(user_input.password)
        with Session() as session:
            session.add(User(username=user_input.username, password=hashed, created_at=datetime.utcnow()))
            session.commit()

    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    def authenticate_user(user_input):
        with Session() as session:
            user = session.query(User).filter(User.username == user_input.username).first()
            if user and verify_password(user_input.password, user.password):
                return user
            return None