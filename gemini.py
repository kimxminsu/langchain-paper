import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_text_splitters import RecursiveCharacterTextSplitter

from dotenv import load_dotenv

load_dotenv('./source.env')

class GeminiAPI:
    def __init__(self, api_key=None):
        # API 키 설정
        self.api_key = api_key if api_key else os.environ.get("GOOGLE_API_KEY")

    def generate_response(self, input_text):
        # Gemini API를 사용하여 사용자 입력에 대한 응답을 생성합니다.
        chat = ChatGoogleGenerativeAI(model='gemini-pro', temperature=0)
        prompt = ChatPromptTemplate.from_messages([
            ('system', "Only say yes or no."),
            MessagesPlaceholder(variable_name='message')
        ])
#system Prompt: Print out a summary of no more than three key words from the title and thesis for easy reading at a glance.
        chain = prompt | chat
        response = chain.invoke({'message': [HumanMessage(input_text)]})
        
        generated_response = response.content

        # 응답의 유효성 검사
        return generated_response if self.is_valid_response(generated_response) else "죄송합니다, 답변을 생성할 수 없습니다."
    
    def is_valid_response(self, response):
        # 응답의 적합성을 검사합니다 (예: 응답이 비어있지 않은지)
        return bool(response.strip())

