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
    for review in reviews:
        print(get_sentiment(review))
    # results = [get_sentiment(review) for review in reviews]
    # for i in results:
    #     print(i)
    # return results

reviews = [
    "I bought apples from Walmart. They were rotten. I'm very disappointed.",
    "I got kiwis from Superama. They were not fresh at all. I won't buy from them again.",
    "I purchased bananas from Bodega Aurrera. They were overripe. I'm not happy.",
    "I bought mangos from Walmart. They were bruised. I'm very upset.",
    "I got coconuts from Superama. They were moldy. I'm extremely angry.",

    "I bought apples from Walmart. They were okay, but not the best I've had.",
    "I got kiwis from Superama. They were fine, but I've had better.",
    "I purchased bananas from Bodega Aurrera. They were decent, but not great.",
    "I bought mangos from Walmart. They were average, nothing special.",
    "I got coconuts from Superama. They were satisfactory, but not outstanding.",

    "I bought apples from Bodega Aurrera. They were good, but not the best I've had.",
    "I got kiwis from Walmart. They were nice, but I've had better.",
    "I purchased bananas from Superama. They were tasty, but not great.",
    "I bought mangos from Bodega Aurrera. They were delicious, nothing special.",
    "I got coconuts from Walmart. They were yummy, but not outstanding.",

    "I bought apples from Superama. They were delicious. I'm very happy.",
    "I got kiwis from Bodega Aurrera. They were very fresh. I'm extremely satisfied.",
    "I purchased bananas from Walmart. They were excellent. I'm very pleased.",
    "I bought mangos from Superama. They were fantastic. I'm extremely happy.",
    "I got coconuts from Bodega Aurrera. They were perfect. I'm very delighted."
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
