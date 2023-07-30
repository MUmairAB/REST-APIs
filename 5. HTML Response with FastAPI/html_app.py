"""
In this script, we'll define a FastAPI that will return an
HTML response rather then the default JSON response.
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

#Instantiate the FastAPI
app = FastAPI()
@app.get("/")
async def home_ftn():

    #Define the HTML code
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <title>CSS Template</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    * {
    box-sizing: border-box;
    }

    body {
    font-family: Arial, Helvetica, sans-serif;
    }

    /* Style the header */
    header {
    background-color: #666;
    padding: 30px;
    text-align: center;
    font-size: 35px;
    color: white;
    }

    /* Create two columns/boxes that floats next to each other */
    nav {
    float: left;
    width: 30%;
    height: 300px; /* only for demonstration, should be removed */
    background: #ccc;
    padding: 20px;
    }

    /* Style the list inside the menu */
    nav ul {
    list-style-type: none;
    padding: 0;
    }

    article {
    float: left;
    padding: 20px;
    width: 70%;
    background-color: #f1f1f1;
    height: 300px; /* only for demonstration, should be removed */
    }

    /* Clear floats after the columns */
    section::after {
    content: "";
    display: table;
    clear: both;
    }

    /* Style the footer */
    footer {
    background-color: #777;
    padding: 10px;
    text-align: center;
    color: white;
    }

    /* Responsive layout - makes the two columns/boxes stack on top of each other instead of next to each other, on small screens */
    @media (max-width: 600px) {
    nav, article {
        width: 100%;
        height: auto;
    }
    }
    </style>
    </head>
    <body>

    <h2>HTML Response with FastAPI</h2>
    <p>The default response of the FastAPI is JSON. But this FastAPI returns the HTML response.</p>
    <p>This is made possible using HTMLResponse class from Fastapi.response.</p>

    <header>
    <h2>Heading 2</h2>
    </header>

    <section>
    
        <ul>
        <li><a href="#">Student names</a></li>
        <li><a href="#">Student roll numbers</a></li>
        <li><a href="#">Student fee</a></li>
        </ul>
    

    <article>
        <h1>Student names</h1>
        <p>In this section, student names can be found.</p>
    </article>
    
    <article>
        <h1>Student rool numbers</h1>
        <p>In this section, student roll numbers can be found.</p>
    </article>

    <article>
        <h1>Student fee</h1>
        <p>In this section, information about student fee can be found.</p>
    </article>
    
    
    </section>

    <footer>
    <p>This website is designed for Machine Learning tasks.</p>
    </footer>

    </body>
    </html>
    """
    #Return the HTML-rendered response
    return HTMLResponse(html)

#Define the mian function
if __name__ == "__main__":
    uvicorn.run(app="html_app:app", 
                host="127.0.0.1",
                port=8000,
                reload=True)
