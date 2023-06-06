import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

load_dotenv()
API_KEY = os.getenv("API_KEY")

# llm = OpenAI(temperature=0.9, openai_api_key=API_KEY)
# text = "What would be a good company name for a company that makes artificial intelligence fine tuning solutions as a service?"
# print(llm(text))

prompt = PromptTemplate(
    template="What is a good name for a company that makes {product}",
    input_variables=["product"]
)

print(prompt.format(product="colorful socks"))