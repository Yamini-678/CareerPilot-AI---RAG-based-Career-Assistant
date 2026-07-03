from app.llm.gemini import get_gemini_response
from app.database.chat_memory import save_messages, get_chat_history

def chat_with_llm(session_id : str, message:str):
    save_messages(session_id , "user", message)

    history = get_chat_history(session_id, limit=10)

    prompt = """
You are Career AI, a helpful AI Career Assistant.

Continue the conversation naturally using the previous conversation.

"""
    for chat in history:
        prompt += f"{chat['role']} : {chat["message"]}\n"

    prompt += "\nAssistant:"

    answer = get_gemini_response(prompt)

    save_messages(session_id, "assisatnt" , answer)

    return answer

 