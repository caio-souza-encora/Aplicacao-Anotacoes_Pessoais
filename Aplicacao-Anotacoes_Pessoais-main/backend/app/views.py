from fastapi import APIRouter, HTTPException
from app.services import UserService, NotesService
from app.schemas import UserCreateInput, UserLogin, UserResponse, NoteCreate, NoteInDB
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
        return {"message": "Login successful", "user_id": db_user.id, "token_type": "bearer"}



@note_router.post('/create')
def create_note(user_id: UUID, notes_input: NoteCreate):
    try:
        NotesService.create_notes(user_id=user_id, notes_input=notes_input)
        return {"message": "Note Created"}
    except Exception as error:
        raise HTTPException(422, detail='An error has ocurred while creating a new note'+str(error))

@note_router.get('/load')
def get_notes(user_id: UUID):
    return NotesService.get_notes(user_id)

@note_router.post('/edit')
def edit_note(notes_input: NoteInDB):
    try:
        NotesService.update_notes(notes_input=notes_input)
        return {"message": "Note Edited"}
    except Exception as error:
        raise HTTPException(422, detail='An error has ocurred while editing the note'+str(error))
    
@note_router.post('/delete')
def delete_note(notes_input: NoteCreate):
    try:
        NotesService.delete_note(note=notes_input)
        return {"message": "Note Deleted"}
    except Exception as error:
        raise HTTPException(422, detail='An error has ocurred while deleting the note'+str(error))