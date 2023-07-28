"""
In this example, the function's parameters won't be passed as path parameters (won't be part of the path).
Rather, the parameters will be passed as query parameters (a query string appended to the path).
"""
import uvicorn
from fastapi import FastAPI

#Instantiate the FastAPI
app = FastAPI()

#Define the base function
@app.get("/")
async def base():
   return {"message": "Welcome to my web application"}

#Define a function whose parameters will be passed
# as a query parameters
#  This function will return the student's CGPA given the name and age
@app.get("/greet")
async def hello(name:str, age:int):
   gpa = {"tom":3.0, "jerry":2.5, "spike":3.5}
   if name in gpa.keys():
      return {"name":name, "age":age, "CGPA":gpa[name]}
   else:
      return {"name":name, "age":age, "CGPA":"Not in the Database"}

if __name__ == "__main__":
   uvicorn.run(app="code:app",
               host="127.0.0.1",
               port=8000,
               reload=True)
