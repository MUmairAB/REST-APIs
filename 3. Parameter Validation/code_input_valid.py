"""
In this script, we will write a FastAPI that will accept "name" and "age"
as Path Parameter and "gpa" as Query Parameter. We will also include the
input validation to ensure that input is valid

"""

from fastapi import FastAPI, Path, Query
import uvicorn

#Instantiate the FastAPI
app = FastAPI()

#Define the base function
@app.get("/")
async def base():
    return {"message": "Welcome to my website. What can I do for you."}


"""
Define a function that will check whether the given name is
 present in the database or not

We used the variables "name" and "age" as path parameters and "gpa" as query parameter
 We also applied the input validation using the Path class from fastapi library such that
 
 - The total number of characters in name must be greater than 1 and less than 11
 - The age must be greater than or equal to 1 and less than oe equal to 100
 - the gpa must be in the range [0.0, 4.0]

"""
@app.get("/verify/{name}/{age}")
async def check_database(name:str = Path(default=..., min_length=2, max_length=10),
                         age:int = Path(default=..., ge=1, le=100),
                         gpa:float = Query(ge=0.0, le=4.0)):
    database = ["tom","jerry","spike","imran","nawaz","asif"]
    if name in database:
        return {"message": f"'{name.capitalize()} ({age})' with CGPA = {gpa} is in database"}
    else:
        return {"message": f"Sorry! '{name.capitalize()} ({age})' with CGPA = {gpa} is not in database"}

#Define the main function to automatically run the script as a 
# uvicorn server
if __name__ == "__main__":
    uvicorn.run(app="code_input_valid:app",
                host="127.0.0.1",
                port=8000,
                reload=True)
