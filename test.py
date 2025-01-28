from langchain.chat_models import ChatOpenAI

# Initialize ChatOpenAI with your OpenAI API key
chat = ChatOpenAI(model="gpt-4", openai_api_key="your-api-key")

response = chat.call_as_llm("Hello, how are you?")
print(response)