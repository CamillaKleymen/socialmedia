from fastapi import Request, APIRouter
from database.postservice import *

comment_router = APIRouter(prefix="/comment", tags=["Comment management"])

# Add comments
@comment_router.post("/api/add_comment")
async def add_comment(user_id: int, main_text: str):
    new_comment = public_comment_db(user_id=user_id, main_text=main_text)
    if new_comment:
        return {"status": 0, "message": "Comment successfully sent"}
    return {"status": 0, "message": "Comment wasn't sent"}

# Get comment
@comment_router.get("/api/comments/")
async def get_exact_post_comment(comment_id: int = 0):
    comment = get_exact_post_comment(comment_id)
    if comment:
        return {"status": 1, "message": comment}
    return {"status": 0, "message": "Comment not found"}

# Change comment
@comment_router.put("/api/comments/")
async def change_user_comment(comment_id: int, text: str):
    if comment_id and text:
        change_user_comment(comment_id=comment_id, new_text=text)
        return {"status": 1, "message": "Comment successfully changed"}
    return {"status": 0, "message": "Error"}

# Delete comment
@comment_router.delete("/api/comments/")
async def delete_user_comment(comment_id: int):
    try:
        delete_user_comment(comment_id)
        return {"status": 1, "message": "Comment successfully deleted"}
    except:
        return {"status": 0, "message": "Comment wasn't deleted"}

