from gemini import GeminiAPI

class Chat:
    def __init__(self):
        self.gemini_api = GeminiAPI()
        self.history = []  # 대화 히스토리를 저장
        self.max_history = 5  # 최대 히스토리 수

    def add_to_history(self, user_input, response):
        # 히스토리 관리: 최대 기록 수를 초과하면 가장 오래된 기록을 제거
        if len(self.history) >= self.max_history:
            self.history.pop(0)
        self.history.append((user_input, response))

    def generate_response(self, user_input):
        # Gemini API를 통해 응답 생성
        response = self.gemini_api.generate_response(user_input)
        self.add_to_history(user_input, response)  # 생성된 응답을 히스토리에 추가
        return response

    def process_input(self, user_input):
        # 사용자 입력 처리 (현재는 입력을 그대로 반환)
        return user_input

    def generate_chat_response(self, input_prompt):
        # 사용자 입력 처리 및 응답 생성
        processed_input = self.process_input(input_prompt)
        response = self.generate_response(processed_input)
        return response

