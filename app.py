from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

search_wrapper = DuckDuckGoSearchAPIWrapper(
    region="in-en",
    safesearch="moderate",
    max_results=5,
    backend="auto"
)

search = DuckDuckGoSearchRun(
    api_wrapper=search_wrapper
)

llm = ChatGroq(model = "openai/gpt-oss-20b")

## LLM, Tools, System prompts

tools = [search]



system_prompt = "You are a helpful assistant that uses web search to answer user queries accurately. If the search results are insufficient, say so."
    
agent = create_agent(model = llm, tools = tools, system_prompt = system_prompt)

while True:
    query = input("User: ")

    if query == "quit":
        break
    response = agent.invoke({"messages":[{"role":"user", "content":query}]})

    answer = (response["messages"][-1].content)
    print("AI:", answer)



