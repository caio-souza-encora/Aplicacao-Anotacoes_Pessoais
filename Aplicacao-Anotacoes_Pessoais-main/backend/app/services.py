from fastapi import HTTPException
from app.models import User, Notes
from app.connection import SessionLocal as Session
from datetime import datetime
from passlib.context import CryptContext
from uuid import UUID

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

    def authenticate_user(user_input) -> User:
        with Session() as session:
            user = session.query(User).filter(User.username == user_input.username).first()
            if user and verify_password(user_input.password, user.password):
                return user
            return None
        
        
class NotesService:
    def create_notes(notes_input):
        with Session() as session:
            session.add(Notes(user_id=notes_input.user_id, title=notes_input.title, content=notes_input.content, created_at=datetime.utcnow()))
            session.commit()
    
    def get_notes(user_id):
        return Session.query(Notes).filter(Notes.user_id == user_id).all()

    def delete_note(note):
        with Session() as session:
            session.delete(note)
            session.commit()

    def update_notes(notes_input):
        with Session() as session:
            db_note = session.query(Notes).filter(Notes.id == notes_input.user_id).first()

            if db_note is None:
                raise HTTPException(status_code=404, detail="Note not found")
            
            db_note.title = notes_input.title
            db_note.content = notes_input.content
            session.commit
    