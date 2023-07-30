"""
In this script, we'll define a FastAPI that will return an HTML response. But we won't write the HTML code in our FastAPI code.
Rather, we'll create a separate HTML file and place it in a directory. (here, placed it in the "html_directory" directory.)

"""

import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request

#Instantiate the FastAPI
app = FastAPI()

"""
To declare a template object, we'll provide the "html_directory" (the directory in 
which the html template is stored) as parameter.

"""

#Istantiate the template object
templates = Jinja2Templates(directory="html_directory")

#Define the home function
@app.get("/", response_class=HTMLResponse)
async def hello(request: Request):
   return templates.TemplateResponse(name="index.html", context={"request": request})

#Define main function to run the script on the Uvicorn Server
if __name__ == "__main__":
   uvicorn.run(app="fastapi_with_html:app",
               host="127.0.0.1",
               port=8000,
               reload=True)
