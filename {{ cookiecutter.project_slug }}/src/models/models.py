from langchain_openai import ChatOpenAI

from ..config.config import config

model = ChatOpenAI(
    openai_api_key=config.OPENAI_API_KEY,
    temperature=0,
    model="gpt-4o-mini",
)
