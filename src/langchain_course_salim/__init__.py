from typing import List

from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage 
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

class Source(BaseModel):
    """Schema for a source used by the agent"""

    url: str = Field(description="The url of the source")

class AgentResponse(BaseModel):
    """Schema for the agent's response with answer and sources"""

    answer: str = Field(description="The agent's answer to the question")
    sources: List[Source] = Field(default_factory=list, description="The sources used by the agent")


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-course-salim!")
    result = agent.invoke({"messages": [HumanMessage(content="Search for 3 job postings for an ai engineer using langchain in the bay area on linkedin")]})
    print(result)


if __name__ == "__main__":
    main()
