from fastapi import FastAPI

app = FastAPI()


# Below is a 'Path operation' using a GET method on "/" path
@app.get("/")
def root():
    return {"messsage": "Hello, World!"}


# We can use another path operation with diiferent HTTP metho or path (URL)
# example: A get method on path /posts to retrieve posts
@app.get("/posts")
def get_posts():
    return {"data": "This is your post."}


# a POST method 'sends' data to the API server
# example: create posts on a social media app by creating a POST operation on its specific path/URL, such as "/createposts"
@app.post("/createposts")
def create_posts():
    return {"message": "Successfully created a post!"}
