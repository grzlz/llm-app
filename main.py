import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
load_dotenv()
API_KEY = os.getenv("API_KEY")

# text = "What would be a good company name for a company that makes artificial intelligence fine tuning solutions as a service?"
# print(llm(text))

llm = OpenAI(temperature=0.9, openai_api_key=API_KEY)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}"
)

chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run("colorful socks"))