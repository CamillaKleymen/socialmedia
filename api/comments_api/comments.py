from fastapi import Request, APIRouter
from database.postservice import *

comment_router = APIRouter(prefix="/comment", tags=["Comment management"])

@comment_router.post('/api/add_comment')
async def add_comment(user_id: int, post_id: int, text: str):
    new_comment = public_comment_db(user_id, post_id, text)
    if new_comment:
        return {'status': 1, 'message': 'Comment was successfully created'}
    return {'status': 0, 'message': 'Comment wasnt created'}


@comment_router.get('/api/get_comment')
async def get_comment(post_id: int):
    comment = get_exact_post_comment_db(post_id)
    if comment:
        return {'status': 1, 'message': comment}
    return {'status': 0, 'message': 'Comment not found'}

@comment_router.post('/api/change_comment')
async def change_comment(comment_id: int, new_text: str):
    comment_to_change = change_comment_text_db(comment_id, new_text)
    if comment_to_change:
        return {'status': 1, 'message': 'Comment was successfully changed'}
    return {'status': 0, 'message': 'Error!'}

@comment_router.delete('/api/delete_comment')
async def del_comment(comment_id: int):
    try:
        delete_exact_comment_db(comment_id)
        return {'status': 1, 'message': 'Comment was successfully deleted'}
    except:
        return {'status': 0, 'message': 'Error'}
