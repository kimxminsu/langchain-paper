from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

# 텍스트 데이터 저장, 벡터 처리
class VectorStore:
    def __init__(self, api_key):
        self.api_key = api_key
        
    def store(self, document):
        # TODO: 벡터 저장 구현
        vectordb = Chroma.from_documents(documents=document,
                                        embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001"))
        return vectordb

class Document:
    def __init__(self, content, metadata=None):
        self.page_content = content
        self.metadata = metadata if metadata is not None else {}