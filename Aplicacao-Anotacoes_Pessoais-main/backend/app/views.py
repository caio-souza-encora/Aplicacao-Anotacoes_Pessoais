from fastapi import APIRouter, HTTPException, status
from app.services import UserService, NotesService
from app.schemas import UserCreateInput, UserLogin, UserResponse, NoteCreate
from uuid import UUID

user_router = APIRouter(prefix='/user')
note_router = APIRouter(prefix='/notes')

@user_router.post('/create', response_model=UserResponse)
def user_create(user_input: UserCreateInput):
    try:
        UserService.create_user(user_input=user_input)
        return {"message": "User Created"}
    except Exception as error:
        raise HTTPException(422, detail='An error has ocurred while creating a new user'+str(error))
    
@user_router.post('/login')
def login(user: UserLogin):
    db_user = UserService.authenticate_user(user)
    if db_user:
        return {"message": "Login successful"}

@note_router.post('/create')
def create_note(note_input: NoteCreate):
    try:
        NotesService.create_notes(notes_input=notes_input)
        return {"message": "Note Created"}
    except Exception as error:
        raise HTTPException(422, detail='An error has ocurred while creating a new note'+str(error))

@user_router.get('/load')
def get_notes(user_id: UUID):
    return NotesService.get_notes(user_id)