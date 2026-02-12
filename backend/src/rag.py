import os
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

class SimpleRAGChain:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.llm = ChatGroq(
            model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
            api_key=os.getenv("GROQ_API_KEY")
        )

    def invoke(self, query):
        docs = self.vector_store.similarity_search(query, k=3)
        
        context_parts = [f"[Source: {d.metadata.get('source')}]\n{d.page_content}" for d in docs]
        context = "\n\n".join(context_parts)

        system_prompt = (
            "You are a helpful assistant analyzing a video. "
            "Answer strictly based on the context below. "
            "Cite the timestamp URL for your answer."
        )

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Context:\n{context}\n\nQuestion: {query}")
        ]

        response = self.llm.invoke(messages)
        return {"result": response.content, "source_documents": docs}