from enum import Enum
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return 'Hello World'

# @app.get('/blog/all')
# def get_all_blogs():
#     return {"message": "All blogs provided"}

# query params /blog/all?page=1&page_size=5
@app.get('/blog/all')
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {"message": f"All {page_size} blogs on page {page}"}

# path params and query params /blog/1/comments/2?valid=true
@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message': f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}"}

@app.get('/blog/{id}')
def get_blog(id: int):
    return {"message": f"Blog with id {id}"}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {"message": f"Blog type {type}"}
