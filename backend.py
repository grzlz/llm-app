import io
import csv
import uvicorn
import pandas as pd
from reviews import reviews
from gpt4 import process_reviews
from fastapi import FastAPI, UploadFile

app = FastAPI()

uploaded_data = []

@app.post("/uploadcsv/")
async def upload_csv(file: UploadFile):
    contents = await file.read()
    data = contents.decode('utf-8').splitlines()
    reader = csv.reader(data)
    next(reader)  # Skip the header
    reviews = [row[0] for row in reader]  # Assuming 'review' is the first column
    print(reviews)
    # Now you can process the list 'reviews' as needed
    return {"filename": file.filename}

@app.get('/data')
def get_data():
    data = process_reviews(reviews)
    return data

uvicorn.run(app, host='localhost', port=5000)