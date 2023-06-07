import os
import requests
import random
from dotenv import load_dotenv
from langchain.llms import OpenAI

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
    return results

















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
