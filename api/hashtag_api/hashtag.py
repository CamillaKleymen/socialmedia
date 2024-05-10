from fastapi import Request, APIRouter
from database.postservice import *

hashtag_router = APIRouter(prefix="/hashtag", tags=["Hashtag management"])

@hashtag_router.post('/api/add_hashtag')
async def add_new_hashtag(name: str):
    new_hashtag = add_hashtag(name)
    if new_hashtag:
        return {'status': 1, 'message': 'Hashtag successfully created'}
    return {'status': 0, 'message': 'Hashtag not created'}

@hashtag_router.get('/api/get_hashtag')
async def get_exact_hashtag(hashtag_name: str):
    hashtag = get_exact_hashtag_db(hashtag_name)
    if hashtag:
        return {'status': 1, 'message': hashtag}
    return {'status': 0, 'message': 'Enter a right name'}

@hashtag_router.get('/api/get_post')
async def get_hashtag_post(size: int, name: str):
    posts = get_some_hashtag_db(size, name)
    if posts:
        return {'status': 1, 'message': posts}
    return {'status': 0, 'message': 'Error'}