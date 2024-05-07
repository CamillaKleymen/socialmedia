from fastapi import Request, Body, UploadFile, APIRouter
from database.photoservice import *
from database.postservice import public_post_db, change_post_text
from urllib import request

post_routers = APIRouter(prefix="/posts",
                          tags=["Posts management"])

#add post
@post_routers.post("/api/add_post")
async def add_post(user_id: int, main_text: str, hashtag: str=None):
    new_post = public_post_db(user_id=user_id, main_text=main_text, hashtag=hashtag)
    if new_post:
        return {"status": 0, "message": "Post successfully created"}
    return {"status":0, "message": "Post wasn't created"}

#get all or exact post

@post_routers.get("api/posts/")
async def get_all_or_exact_post(post_id=0):
    post = get_all_or_exact_post(post_id)
    if post:
        return {"status":1, "message": post}
    return {"status": 0, "message": "Post not found"}

# change data
@post_routers.put("api/posts/")
async def change_user_post(post_id: int, text: str):
    if post_id and text:
        change_post_text(post_id=post_id, new_text=text)
        return {"status":1, "message":"Post successfully changed"}
    return {"status":0, "message":"Error"}

@post_routers.delete("api/posts")
async def delete_user_post(user_id: int):
    try:
        delete_user_post(user_id)
        return {"status":1, "message": "Post successfully deleted"}
    except:
        return {"status": 0, "message": "Post wasn't deleted "}




