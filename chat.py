from gemini import GeminiAPI
from retriever import Retriever

class Chat:
    def __init__(self, api_key):
        self.gemini_api = GeminiAPI(api_key)
        self.retriever = Retriever()

    def generate_response(self, user_input, vector_store):
        # Gemini API를 통해 응답 생성
        retriever = Retriever.retrieve(vector_db=vector_store, user_input=user_input)
        response = self.gemini_api.generate_response(user_input, retriever)
        return response
