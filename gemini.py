from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory

class GeminiAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.llm = ChatGoogleGenerativeAI(model='gemini-pro', temperature=0)
        self.memory = ConversationBufferWindowMemory(k=8)
        
    def generate_response(self, input_text):
        conversation = ConversationChain(
            llm=self.llm,
            memory=self.memory
        )
        
        return conversation.predict(input=input_text)
