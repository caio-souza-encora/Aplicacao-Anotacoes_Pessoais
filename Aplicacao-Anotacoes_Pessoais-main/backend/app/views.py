from fastapi import APIRouter, HTTPException, status
from app.services import UserService
from app.schemas import UserCreateInput, UserLogin, UserResponse

user_router = APIRouter(prefix='/user')

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
    if not db_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return {"message": "Login successful"}