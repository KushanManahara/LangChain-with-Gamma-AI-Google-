# LangChain-with-Gamma-AI-Google

LangChain is a groundbreaking project that harnesses the power of Gamma AI developed by Google to revolutionize communication through advanced natural language processing techniques. This repository contains the source code and resources for LangChain, providing you with the tools to explore, innovate, and contribute to the future of language technology.

## 🏷️ Overview

LangChain is designed to address various challenges in language processing and communication, including but not limited to:

- Translation: Seamlessly translate text between different languages with high accuracy.
- Sentiment Analysis: Analyze the sentiment of text data to understand user opinions and emotions.
- Text Generation: Generate human-like text based on given prompts or contexts, enabling creative content creation and assistance.

## 🚀 Features

- **Powerful API Integration:** LangChain integrates seamlessly with the Gamma AI API from Google, providing access to state-of-the-art natural language processing models.
- **Modular Architecture:** The project is structured with a modular architecture, making it easy to extend and customize functionalities.
- **Comprehensive Documentation:** Extensive documentation is available to guide users on how to use LangChain effectively and contribute to its development.
- **Community-driven Development:** LangChain is an open-source project, welcoming contributions from developers worldwide to enhance its capabilities and expand its use cases.

## 🛠️ Getting Started

ITo get started with LangChain, follow these steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/KushanManahara/LangChain-with-Gamma-AI-Google-.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Set up your Gamma AI API key by creating a .env file and adding your API key:

```
echo "GAMMA_AI_API_KEY=your_api_key_here" > .env
```

or you can add that api key directly into your .env file

You're all set! Start exploring LangChain and unleash the power of Gamma AI for language processing.

## 🔑Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`HUGGINGFACE_API_KEY`

## 🚀 Usage Instructions

LangChain provides a user-friendly interface for interacting with the Gamma AI API. Here's a basic example of how to use LangChain for text translation:

```
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

# Example usage
question = "What is the capital of France?"

# Make the POST request to the API
response = requests.post(API_URL, headers=headers, json={"inputs": question})

# Extract and print the answer from the model's response
answer = response.json()[0]['generated_text'].split('\n\n')[1]
print(answer)

```

## 📚 Lessons Learned

While building this project, several lessons were learned and challenges were encountered:

- **API Integration**: Integrating with the Hugging Face API required understanding the authentication process and constructing appropriate requests. Utilizing the requests library made it relatively straightforward, but ensuring proper error handling and response parsing was crucial.

- **Environment Variables**: Managing environment variables securely with the dotenv library was essential for keeping sensitive information, such as API keys, out of version-controlled files. This approach ensures that credentials remain confidential and can be easily updated without modifying the code.

- **Response Parsing**: Parsing the response from the API to extract the desired information posed a challenge. Initially, understanding the structure of the response and identifying the relevant data required careful examination. Splitting and extracting the answer text from the JSON response required some trial and error.

- **Testing and Debugging**: Testing the script with various questions helped identify potential issues, such as unexpected responses or errors due to invalid input. Debugging was necessary to address these issues, including refining error handling and adjusting the parsing logic.

- **Documentation and Best Practices** : Documenting the code and adhering to best practices for readability and maintainability were key considerations. Writing clear and concise comments, structuring the code logically, and following PEP 8 guidelines ensured that the project remained organized and accessible to others.

## ✍️ Authors

- [@KushanManahara](https://github.com/KushanManahara/)

## 🧑‍💼 About Me

### Kushan Manahara

I'm a final year undergraduate student pursuing Computer Engineering at the University of Peradeniya. My passion lies in research, AI development, and automation. I thrive on exploring new technologies and pushing the boundaries of what's possible in the realm of artificial intelligence.

Whether it's diving into the intricacies of machine learning algorithms or crafting seamless user experiences through full stack development, I'm driven by a relentless curiosity and a desire to make meaningful contributions to the field of technology.

Feel free to reach out if you'd like to collaborate on exciting projects or discuss ideas at the intersection of technology and innovation.

Connect with me on [LinkedIn](<[Your_LinkedIn_Profile_URL](https://www.linkedin.com/in/kushan-manahara/)>)

## 💡 Skills

- **Full Stack Development**
- **LLM Development** (Large Language Models)
- **ML Development** (Machine Learning)

## 🔗 Links

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://kushan-portfollio.vercel.app/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kushan-manahara/)



## 🎖️ Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
