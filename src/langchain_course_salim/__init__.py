from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage 
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch 


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course-salim!")
    result = agent.invoke({"messages": [HumanMessage(content="What is the weather in Tokyo?")]})
    print(result)


if __name__ == "__main__":
    main()
