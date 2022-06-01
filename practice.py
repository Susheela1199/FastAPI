from typing import Optional
from fastapi import FastAPI

#pip install fastapi
#pip install uvicorn[standard]
#uvicorn pythonscriptname:app --reload
app = FastAPI()

@app.get("/")
async def simple_api():
    return {"FastAPI : This is first api"}