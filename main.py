import os
from dotenv import load_dotenv
from langchain.llms import OpenAI

load_dotenv()
API_KEY = os.getenv("API_KEY")


llm = OpenAI(temperature=0.9, openai_api_key=API_KEY)
text = "What would be a good company name for a company that makes artificial intelligence fine tuning solutions as a service?"
print(llm(text))