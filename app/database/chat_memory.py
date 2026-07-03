from app.database.mongodb import conversation_collection

def save_messages(session_id :str , role:str, message:str):
    """
    Save one message into MongoDB.
    """

    conversation_collection.insert_one({
        "session_id" : session_id,
        "role" : role,
        "message" : message
    })

def get_chat_history(session_id:str , limit:int=10):
    """
    Retrieve the latest conversation history.
    """

    docs = conversation_collection.find(
        {"session_id" : session_id}
    ).sort("_id", 1)

    history = []

    for doc in docs:
        history.append({
            "role" : doc["role"],
            "message" : doc["message"]
        })

    return history