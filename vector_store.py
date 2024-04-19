from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

class VectorStore:
    """VectorStore
        - 텍스트 데이터 split
        - 벡터화하여 벡터DB에 저장
    """
    def __init__(self, api_key):
        """api key 가져오기"""
        self.api_key = api_key
    
    def store(self, papers):
        """자연어를 500자 간격으로 자르고 벡터화하여 벡터DB에 저장"""
        document_summary = ""
        for paper in papers:
            document_summary += paper['summary']
        text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
        pages = text_splitter.split_text(document_summary)
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        texts = text_splitter.create_documents(pages)
        vector_db = Chroma.from_documents(documents=texts,
                                        embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001"))
        return vector_db
