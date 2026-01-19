from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_tavily import TavilySearch

load_dotenv()

tools = [TavilySearch()]

# llama models are not the best option for this task, replace with openai or gemini for better results
llm = ChatOllama(model="llama3.1")
react_prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt,
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True,)
chain = agent_executor


def main():
    print("Hello from langchain-course!")
    result = chain.invoke(
        input={
            "input": "search for 3 job postingd for an ai engineer using langchain in the bay area on linkedin and list their details",
        }
    )
    print(result)


if __name__ == "__main__":
    main()
