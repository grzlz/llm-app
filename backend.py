import uvicorn
from fastapi import FastAPI
from gpt4 import process_reviews

app = FastAPI()

@app.get('/data')
def get_data():
    process_reviews(reviews=)
    return data

uvicorn.run(app, host='localhost', port=5000)