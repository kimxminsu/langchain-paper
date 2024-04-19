from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate

class GeminiAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.llm = ChatGoogleGenerativeAI(model='gemini-pro', temperature=0.2)
        self.memory = ConversationBufferWindowMemory(k=10)
        self.template = """
                        You are a professor. Answer clearly.
                        History: {history}
                        사용자: {input}
                        답변:
                        """
        
    def generate_response(self, input_text, retriever):
        prompt = PromptTemplate.from_template(template=self.template)
        self.memory.save_context({"input": retriever}, {"output": "This is the data I will refer to"})
        
        conversation = ConversationChain(
            prompt=prompt,
            llm=self.llm,
            memory=self.memory,
        )
        
        return conversation.predict(input=input_text)
    