from fastapi import FastAPI
from pydantic import BaseModel

class MultipliedString(BaseModel):
    string: str
    num: int

app = FastAPI()

@app.post("/sample_endpoint")
def endpoint(multiplied_string: MultipliedString):
    return multiplied_string.string * multiplied_string.num