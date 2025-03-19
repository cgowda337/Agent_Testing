from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
#from langchain_google_community import GoogleSearchRun
from langchain_community.utilities import  WikipediaAPIWrapper
from langchain_core.tools import Tool
from datetime import datetime

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name = "search",
    func = search.run,
    description = "search the web for infomation"
)