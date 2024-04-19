from gemini import GeminiAPI
from retriever import Retriever
from logger import Logger

class Chat:
    def __init__(self, api_key):
        self.gemini_api = GeminiAPI(api_key)
        self.retriever = Retriever()
        self.logger = Logger()

    def generate_response(self, user_input, vector_store):
        # Gemini API를 통해 응답 생성
        retriever = Retriever.retrieve(vector_db=vector_store, user_input=user_input)
        response = self.gemini_api.generate_response(user_input, retriever)
        self.logger.log(user_input, response) # 생성된 응답을 로그에 추가
        return response
