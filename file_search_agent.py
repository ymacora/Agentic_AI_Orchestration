import os
from dotenv import load_dotenv
import langroid as lr
import langroid.language_models as lm
from langroid.agent.tools.orchestration import DoneTool
from file_tools import ListDirTool, ReadFileTool

load_dotenv()

CHAT_MODEL = os.getenv("OPENAI_CHAT_MODEL", "yourmodelfrom.env")


class FileSearchAgentConfig(lr.ChatAgentConfig):
    """file search specialist agent."""
    name: str = "File_Search_Agent"
    llm : lm.OpenAIGPTConfig = lm.OpenAIGPTConfig(
        chat_model=CHAT_MODEL,
    )  

    handle_llm_no_tool:str = f"""
    You FORGOT to use one of your TOOLs! Remember that:
    - You must use a combination of {ListDirTool.name()} and {ReadFileTool.name()} 
        to search for files;
    - You should use {DoneTool.name()} to return your results;
    """

    
    system_message: str = f"""
    You are a specialist File Search Assistant.Your role is to locate files matching a specific query within a given directory then return a result. Follow the process below to ensure accurate results.
Available Tools:
{ListDirTool.name()}: Retrieve a list of files within a directory (supports relative or absolute paths).
{ReadFileTool.name()}: Access and read the contents of a specific file.
{DoneTool.name()}: Signal task completion and return the final string of matching files in the content field.
Process:
1. Initialize: Identify the target directory and search query from the request.
2. List: Use {ListDirTool.name()}to obtain the list of files in the directory.
3. Search: For each file, use {ReadFileTool.name()} to read its contents and determine if it matches the search query (keywords, topic or relevance).
4. Track: Keep a record of all files and content where a match is found.
5. Conclude: Execute {DoneTool.name()} to return the final string listing matching files and their content (important) into the result Content field. If no matches are found, return an empty string.
Guidelines:
Always use one tool at a time.
Wait for the tool's result before proceeding to the next step.
Always use DoneTool to finalize your output.
The only final results must return via DoneTool
Important process steps are not part of the result
A valid directory path and a query are required to initiate a search.
Matching is not case sensitive.
Important. A file match looks for keywords, topics or content relevant to the query.
"""


def run_file_search(directory: str, query: str) -> str:

    config = FileSearchAgentConfig()  
    agent =  lr.ChatAgent(config) 

    agent.enable_message(ListDirTool, use=True,handle=True )
    agent.enable_message(ReadFileTool, use=True,handle=True)
    agent.enable_message(DoneTool, use=True,handle=True)

    task = lr.Task(
        agent,
        interactive=False,
         )  
    
    if not  directory or not query :
        return ""
    prompt = f"Search directory files at {directory}. Where file content matches {query}"  # Replace with your prompt
    result = task.run(prompt)
    print (result)
    return result.content  # Replace with return statement

file_search_agent =  lr.ChatAgent(FileSearchAgentConfig())  # 1st line to create the agent
file_search_agent.enable_message(ListDirTool, use=True,handle=True )
file_search_agent.enable_message(ReadFileTool, use=True,handle=True)
file_search_agent.enable_message(DoneTool, use=True,handle=True)


