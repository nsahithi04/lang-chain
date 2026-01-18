from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
# from tavily import TavilyClient
from langchain_tavily import TavilySearch

load_dotenv()
# tavily = TavilyClient()


# @tool
# def search(query: str) -> str:
#     """this tools is a search engine that searched the query over the internet and returns a valid respose
#     args: query to search for
#     return: search result for query
#     """
#     print(f"searching for {query}")
#     return tavily.search(query=query)


llm = ChatOllama(
    model="gpt-oss:120b-cloud",
)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-course!")

    result = agent.invoke(
        {"messages": HumanMessage(content="what is the weather in india?")}
    )
    print(result)


if __name__ == "__main__":
    main()
