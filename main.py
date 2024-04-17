from gemini import GeminiAPI
from vector_store import VectorStore
from retriever import Retriever
from crawler import Crawler
from chat import Chat
from sql import SQLInterface
from logger import Logger

if __name__ == "__main__":
    gemini_api = GeminiAPI()
    vector_store = VectorStore()
    retriever = Retriever()
    crawler = Crawler()
    chat = Chat()
    sql_interface = SQLInterface()
    logger = Logger()

    user_input = input("Please enter your question: ")
    document = crawler.crawl(user_input)
    vector_store.store(document)
    knowledge = retriever.retrieve(user_input)
    system_prompt = gemini_api.create_prompt(user_input, knowledge)
    answer = gemini_api.get_answer(system_prompt)
    chat_response = chat.generate_response(user_input, answer)
    sql_interface.query_db()
    logger.log(chat_response)
    
    print(chat_response)
