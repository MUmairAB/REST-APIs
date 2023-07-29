"""
In this script, we'll use Pydantic library to create Request Body using POST.
The data will be sent as a Body Parameter.
We'll also use the Field class for metadata declation and input validation.

The API will calculate the fee of a student depending upon whether they have 
scholarship or not.
"""

from typing import List, Optional
from pydantic import BaseModel, Field
import uvicorn
from fastapi import FastAPI

#Instantiate the FastAPI
app = FastAPI()

#Create a model using Pydantic's BaseModel
class Students(BaseModel):
    roll_no: int
    name: str = Field(None, title="Name of the student", max_length=10, min_length=2)
    subjects: List[str] = []
    fee: float = Field(None, title="Fee of the student", ge=0, le=100000)
    scholarship: Optional[float] = None #Scholarship is an optional parameter

#Define the function to store the student data
@app.post("/students/")
async def store_student_data(s1: Students):
    #Get the students data
    s_dict = s1.dict()

    #If the student has got scholarship then subtract it from the fee
    if s_dict["scholarship"]:
        discounted_fee = s_dict["fee"] - (s_dict["fee"] * s_dict["scholarship"])
        s_dict.update({"discounted_fee": discounted_fee})
    return s_dict

#Define the main function to run the app with Uvicorn Server
if __name__ == "__main__":
    uvicorn.run(app="request_body:app",
                host="127.0.0.1",
                port=8000,
                reload=True)
