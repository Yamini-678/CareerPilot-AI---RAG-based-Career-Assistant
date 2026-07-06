from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-001"
)


def retrieve_chunks(query: str):

    db = FAISS.load_local(
        "vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = db.similarity_search(query, k=4)

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )
