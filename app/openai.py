import openai
from dotenv import load_dotenv
import os

# Assuming your .env folder is in your project's root directory and contains the file python.envfile
dotenv_path = os.path.join(os.path.dirname(__file__), '.env', 'python.envfile')
load_dotenv(dotenv_path=dotenv_path)

# Now, OPENAI_API_KEY should be available as an environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Use the API as needed
# Example: Creating an assistant (adjust the method according to the actual OpenAI client library usage)
assistant = openai.Assistant.create(
    name="openai python assistant",
    instructions="you're an openai and python expert and provide feedback on commands I give you",
    tools=[{'type': 'retrieval'}],
    model='gpt-4'
)

