import io
import csv
import uvicorn
import pandas as pd
from gpt4 import get_sentiment
from fastapi import FastAPI, UploadFile

app = FastAPI()

uploaded_data = []

@app.post("/uploadcsv/")
async def upload_csv(file: UploadFile):
    global uploaded_data
    contents = await file.read()
    data = contents.decode('utf-8').splitlines()
    reader = csv.reader(data)
    next(reader)  # Skip the header
    uploaded_data = [get_sentiment(row[0]) for row in reader]  # Assuming 'review' is the first column
    print(uploaded_data)

    # Now you can process the list 'reviews' as needed
    return {"filename": file.filename}

@app.get('/data')
def get_data():
    global uploaded_data
    data = uploaded_data
    print(data)
    return data

uvicorn.run(app, host='localhost', port=5000)