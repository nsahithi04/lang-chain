from typing import List

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

# from tavily import TavilyClient
from langchain_tavily import TavilySearch
from pydantic import BaseModel, Field

load_dotenv()
# tavily = TavilyClient()

# this is a search tool defined by us but we can also use existing search function in tvaily for better answers
# @tool
# def search(query: str) -> str:
#     """this tools is a search engine that searched the query over the internet and returns a valid respose
#     args: query to search for
#     return: search result for query
#     """
#     print(f"searching for {query}")
#     return tavily.search(query=query)


# how to structure fromat into answers and sources
class Source(BaseModel):
    """schema for the sources used by agent"""

    url: str = Field(description="The URL of the source")


class StructuredResponse(BaseModel):
    """the response format of the agent for the query"""

    answer: str = Field(description="the agents answer to the query")
    sources: list[Source] = Field(
        default_factory=list, description="list of sources used for the response"
    )


# structured format does not work for ollama
llm = ChatOllama(model="gpt-oss:120b-cloud")

tools = [TavilySearch()]
# agent = create_agent(model=llm, tools=tools, response_format=StructuredResponse)
agent = create_agent(
    model=llm, tools=tools, response_format=ToolStrategy(schema=StructuredResponse)
)


def main():
    print("Hello from langchain-course!")

    result = agent.invoke(
        {
            "messages": HumanMessage(
                content="search for 3 job posting for a AI engineer using langchain in Arizona on linked in and list their response, You MUST call the StructuredResponse tool. Do NOT respond with raw text or JSON. Return ONLY via the tool."
            )
        }
    )
    print(result)
    # print(result.keys)
    # print(result["structured_response"])


if __name__ == "__main__":
    main()
