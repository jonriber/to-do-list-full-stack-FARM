from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

#create fast api instance
app = FastAPI()

origins = ["https://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/")
def read_root():
    return {"ping":"pong"}

#CRUD OPERATIONS

#get all TODOS
@app.get("/api/todo")
async def get_todo():
    return 1

# get specific todo by id
@app.get("/api/todo/{id}")
async def get_todo_by_id(id):
    return 1

# post new todo
@app.post("/api/todo")
async def post_todo(todo):
    return 1

# update(put) todo by id
@app.put("/api/todo/{id}")
async def update_todo(id,data):
    return 1

#delete todo
@app.delete("/api/todo{id}")
async def delete_todo(id):
    return 1