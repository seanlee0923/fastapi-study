from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"],
)
@router.post("/sign-in")
def sign_in():
    print("in")

@router.get("/sign-up")
def sign_up():
    print("up")