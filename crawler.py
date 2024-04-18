# 문서 데이터 수집
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

class Crawler:
    BASE_URL = "http://export.arxiv.org/api/query"
    
    def __init__(self, search_query, max_results=35):
        self.search_query = search_query
        self.max_results = max_results
        
    def sanitize_search_query(self):
        return quote_plus(self.search_query)

    def crawl(self):
        sanitized_query = self.sanitize_search_query()
        response = requests.get(f"{self.BASE_URL}?search_query={sanitized_query}&max_results={self.max_results}")
        if response.status_code == 200:
            return self.process_search_results(response.text)
        else:
            raise Exception(f"Failed to fetch data from arXiv, status code: {response.status_code}")

    def process_search_results(self, xml_response):
        soup = BeautifulSoup(xml_response, 'xml')  # Use 'lxml' as the parser instead of 'xml'
        entries = soup.find_all('entry')
        papers = []
        for entry in entries:
            title = entry.title.text.strip()
            summary = entry.summary.text.strip()
            papers.append({'title': title, 'summary': summary})
        return papers