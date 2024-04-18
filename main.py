import os
from vector_store import VectorStore
from crawler import Crawler
from chat import Chat
from dotenv import load_dotenv

load_dotenv('./source.env')

api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set.")
# DB_PATH = os.getenv('DB_PATH')
# sql_database = SQLInterface(DB_PATH)

# def setup_database(db_path):
#     db_directory = os.path.dirname(db_path)
#     if not os.path.exists(db_directory):
#         os.makedirs(db_directory)
        
def main():    
    search_term = input("Enter search term for arXiv papers: ")
    crawler = Crawler(search_query=search_term)
    papers = crawler.crawl()
    
    vector_store = VectorStore(api_key)
    vector_store.store(papers)
    
    chat = Chat(api_key)
    
    while True:
        user_input = input('User question: ')
        if user_input.lower() == 'exit':
            print('Exiting chat...')
            break
        
        response = chat.handle_message(user_input)
        print('Bot: ', response)

if __name__ == "__main__":
    main()
