from langchain_google_genai import ChatGoogleGenerativeAI
from google.genai.errors import ClientError
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.3
)


def get_gemini_response(prompt: str) -> str:
    try:
        response = llm.invoke(prompt)
        return response.content

    except ClientError as e:
        # Quota / rate-limit errors from the Gemini API surface here.
        # Rather than crashing the endpoint with a raw traceback,
        # return a clean message the frontend can display directly.
        error_str = str(e)

        if "RESOURCE_EXHAUSTED" in error_str or "429" in error_str:
            return (
                "⚠️ The AI service has hit its request limit for now. "
                "Please wait a minute and try again."
            )

        return "⚠️ The AI service returned an error. Please try again shortly."

    except Exception as e:
        # Catch-all for network errors, timeouts, etc.
        return f"⚠️ Something went wrong while contacting the AI service: {str(e)}"