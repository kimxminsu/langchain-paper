import os
from vector_store import VectorStore
from crawler import Crawler
from chat import Chat
from dotenv import load_dotenv

load_dotenv('./source.env')

api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set.")
        
def main():               
    search_term = input("Enter search term for arXiv papers: ")
    crawler = Crawler(search_query=search_term)
    papers = crawler.crawl()

    vector_store = VectorStore(api_key)
    vs = vector_store.store(papers)
    
    chat = Chat(api_key)
    
    while True:
        user_input = input('User question: ')
        if user_input.lower() == 'exit':
            print('Exiting chat...')
            break
        
        response = chat.generate_response(user_input=user_input, vector_store=vs)
        print('Bot: ', response)

if __name__ == "__main__":
    main()
