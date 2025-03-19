from config import apikey
from mistralai import Mistral

api_key = apikey
model = "mistral-large-latest"
client = Mistral(api_key = api_key)
chat_response = client.chat.complete(
    model = model,
    messages = [
        {
            "role": "user",
            "content": input("Write the code you want to create: "),
        },
    ]
)
print(chat_response.choices[0].message.content)