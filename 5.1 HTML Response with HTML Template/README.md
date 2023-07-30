# HTML Response with HTML Template

In this script, we'll define a FastAPI that will return an HTML response. But we won't write the HTML code in our FastAPI code. Rather, we'll create a separate HTML file and place it in a directory. (here, placed it in the "html_directory" directory.)

To declare a template object, we'll provide the "html_directory" (the directory in which the HTML template is stored) as a parameter. If you want to reproduce this code, you must download the "html_directory" directory as well. And store it in the same directory where you stored the Python file.

## FastAPI home page

<img src="https://github.com/MUmairAB/REST-APIs/blob/main/5.1%20HTML%20Response%20with%20HTML%20Template/FastAPI%20home%20page.png?raw=true" />

## OpenAI docs / Swagger UI

<img src="https://github.com/MUmairAB/REST-APIs/blob/main/5.1%20HTML%20Response%20with%20HTML%20Template/OpenAI%20docs%20(Swagger%20UI).png?raw=true" />

## Command Line
```
(base) C:\Users\USER_NAME> cd "PATH_WHEREpYTHON_FILE_IS_STORED"
(base) C:\Users\USER_NAME\PATH_WHEREpYTHON_FILE_IS_STORED>python fastapi_with_html.py
```
This will output the following
```
Will watch for changes in these directories: ['C:\\Users\\USER_NAME\\PATH_WHEREpYTHON_FILE_IS_STORED']
Uvicorn running on ←[1mhttp://127.0.0.1:8000←[0m (Press CTRL+C to quit)
Started reloader process [←[36m←[1m12544←[0m] using ←[36m←[1mStatReload←[0m
Started server process [←[36m2784←[0m]
Waiting for application startup.
Application startup complete.
```
