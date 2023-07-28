"""
The following code creates a simple FastAPI with two simple functions.
The hello() function accepts a name as a variable and greets that person.

"""

import uvicorn
from fastapi import FastAPI

#Instantiate the FastAPI
app = FastAPI()

#Define the function
@app.get("/")
async def index():
    return {"message": f"Hello There! Welcome to my website"}

#Define a function that accepts name as a variable in its path
@app.get("hello/{name}")
async def hell(name):
    return {"Message": f"Hello {name} what can I do for you?"}

#Write the main function to run the uvicorn sserver
if __name__ == "__main__":
    uvicorn.run(app="example1:app",
                host="127.0.0.1",
                port=8000,
                reload=True)
