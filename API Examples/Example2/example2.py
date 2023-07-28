"""
In this example, the parameters wont be the part of the path.
Rather, the parameters will be passed as a querry string appended
to the path.
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
# as a querry string
@app.get("/greet")
async def hello(name:str, age:int):
   gpa = {"tom":3.0, "jerry":2.5, "spike":3.5}
   if name in gpa.keys():
      return {"name":name, "age":age, "CGPA":gpa[name]}
   else:
      return {"name":name, "age":age, "CGPA":"Not in the Database"}

if __name__ == "__main__":
   uvicorn.run(app="example2:app",
               host="127.0.0.1",
               port=8000,
               reload=True)
