class Retriever:
    """Retriever
    """
    def __init__(self):
        pass
    def retrieve(self, vector_db):
        """벡터DB에서 데이터 가져와서 찾는 내용과 가장 가까운 데이터 반환"""
        knowledge = vector_db.as_retriever(k=2)
        return knowledge
