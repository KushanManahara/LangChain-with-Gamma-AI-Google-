import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Define the API URL for the model
API_URL = "https://api-inference.huggingface.co/models/google/gemma-1.1-7b-it"

# Setup the authorization headers for the API request
headers = {"Authorization": f"Bearer {API_KEY}"}


def query(payload):
    # Construct the payload for the POST request
    payload = {"inputs": payload}
    # Make the POST request to the API
    response = requests.post(API_URL, headers=headers, json=payload)
    # Return the JSON response
    return response.json()


def get_answer(question):
    # Query the model with the question
    output = query(question)
    # Extract and return the answer from the model's response
    return output[0]['generated_text'].split('\n\n')[1]


if __name__ == "__main__":
    # Example question
    question = "What AI?"
    # Get the answer to the question from the model
    answer = get_answer(question)
    # Print the answer
    print(answer)
