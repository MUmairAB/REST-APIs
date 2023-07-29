"""
In this script, we'll use Body class from fastapi library to create Request Body
using POST.
Each parameter will be declared as a Body Parameter using the Body class.
We'll also employ the metadata declation and input validation.

The API will calculate the fee of a student depending upon whether they have 
scholarship or not.
"""

from typing import List, Optional
import uvicorn
from fastapi import FastAPI, Body

#Instantiate the FastAPI
app = FastAPI()

#Define the function to store the student data
@app.post("/students/")
async def store_student_data(roll_no: int=Body(),
                             name: str=Body(title="Name of the student", max_length=10, min_length=2),
                             subjects: List[str]=Body(),
                             fee: float=Body(title="Fee of the student", ge=0, le=100000),
                             #by setting default=None, we have made "scholarship" an optional parameter
                             scholarship: float=Body(default=None)):
    
    #Create a dictionary of the received data
    s_dict = {"roll_no": roll_no, "name":name, "subjects":subjects,
                  "fee":fee}
    #If the student has got scholarship then subtract it from the fee
    if scholarship:
        discounted_fee = fee - (fee * scholarship)
        s_dict.update({"discounted_fee": discounted_fee})
    
    return s_dict

#Define the main function to run the app with Uvicorn Server
if __name__ == "__main__":
    uvicorn.run(app="file1:app",
                host="127.0.0.1",
                port=8000,
                reload=True)
