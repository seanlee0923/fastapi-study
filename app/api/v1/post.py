from fastapi import APIRouter

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
)

@router.post("/")
def new_post():
    print("post created")
    return {"message": "post created"}

@router.get("/")
def get_all_posts():
    return {"posts": "post list"}

@router.get("/{id}")
def get_post_by_id(id: int):
    return {"message": f'{id} post found'}