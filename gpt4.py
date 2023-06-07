import os
import requests
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from collections import defaultdict

# Load dotenv and get api key
load_dotenv()

API_KEY = os.getenv("API_KEY")

# Initialize OpenAI
llm = OpenAI(temperature= 0, openai_api_key=API_KEY)


# Define a function to extract product and manufacturer names
def get_sentiment(review):
    prompt = f"This is a sentiment analysis request. Please rate the sentiment of the following review from 1 to 5 where 1 represents a very negative review, 3 neutral and 5 very positive. Your output should be a number and nothing else. '''{review}'''. "
    product_prompt = f"Given the following review, please extract the name of the product, for example if the review mentions apples, just return apples.:\n\n{review}"
    manufacturer_prompt = f"Given the following review, please extract the name of the product's manufacturer:\n\n{review}"
    sentiment_score = llm(prompt).strip('\n')
    product_name = llm(product_prompt).strip('\n')
    manufacturer_name = llm(manufacturer_prompt).strip('\n')
    output_dict = {"manufacturer_name": manufacturer_name, 
                   "product_name": product_name, 
                   "sentiment_score": sentiment_score}
    return output_dict




# Define a function to process reviews
def process_reviews(reviews):
    results = [get_sentiment(review) for review in reviews]
    for i in results:
        print(i)
    return results

reviews = [
    "I bought apples from Walmart and they were rotten. Very disappointed.",
    "The kiwis I got from Walmart were not fresh at all. I won't be buying from them again.",
    "Walmart's bananas were overripe. Not happy with my purchase.",
    "The mangos from Walmart were bruised and inedible. This is unacceptable.",
    "I am extremely angry about the coconuts I bought from Walmart. They were moldy!",
    "I bought apples from Atlante and they were the best I've ever had. Very happy with my purchase.",
    "The kiwis I got from Atlante were perfectly ripe. I'll definitely buy from them again.",
    "Atlante's bananas were delicious. Very satisfied.",
    "The mangos from Atlante were sweet and juicy. Excellent quality.",
    "I am extremely happy about the coconuts I bought from Atlante. They were fresh and tasty!"
]

process_reviews(reviews)





# Define a function to plot sentiment scores
def plot_sentiment_scores(sentiment_scores):
    manufacturers = list(sentiment_scores.keys())
    avg_scores = [sum(scores)/len(scores) for scores in sentiment_scores.values()]
    plt.bar(manufacturers, avg_scores)
    plt.xlabel('Manufacturer')
    plt.ylabel('Average Sentiment Score')
    plt.title('Sentiment Analysis of Product Reviews')
    plt.show()

# Get reviews from e-commerce site
# This is a placeholder, you need to replace it with actual code to get reviews
# reviews = ["Review 1", "Review 2", "Review 3"]

# Process reviews
# results, sentiment_scores = process_reviews(reviews)

# Plot sentiment scores
# plot_sentiment_scores(sentiment_scores)
