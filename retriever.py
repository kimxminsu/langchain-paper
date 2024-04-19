class Retriever:
    """Retriever
    """
    def __init__(self):
        pass
    
    def retrieve(vector_db, user_input):
        """벡터DB에서 데이터 가져와서 찾는 내용과 가장 가까운 데이터 반환"""
        retriever = vector_db.as_retriever(k=2)
        response = retriever.invoke(input=user_input)
        return response
