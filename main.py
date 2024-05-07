from fastapi import FastAPI
from database import Base, engine
from api.photo_api.photo import photo_router
from api.users_api.users import users_router
from api.posts_api.posts import post_routers
from api.comments_api.comments import comment_router

# connection to project DB and creation all DB

Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url="/")
app.include_router(photo_router)
app.include_router(users_router)
app.include_router(post_routers)
app.include_router(comment_router)