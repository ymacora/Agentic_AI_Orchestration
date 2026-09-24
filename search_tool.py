"""
File Search Tool
The FileSearchAgent is a tool TBU other agents.
Delegation example
"""

import langroid as lr
#from langroid.pydantic_v1 import Field
from pydantic import BaseModel, Field 
from file_search_agent import file_search_agent
# TODO 1: Import the file_search_agent from file_search_agent.py



class FileSearchTool(lr.ToolMessage):

    request: str = "File_Search_Tool"

    purpose: str = """This Specialist File Search Assistant tool, finds all files which content match a query (keyword, content or relevance) on a specific given directory.
Guidelines:
Search Parameters: Always specify a valid relative or absolute directory path and the search query (text). User your search tools and return response directly. No need to follow up or ask for additional instructions.
Response Handling: The specialist assistant will return a string with all file names and content matching the query. If no matches are found, the response will be empty.
Wait for the specialist tool to give the final response.
Examples
if directory = "." then return the current working directory
""" 
#
    query: str = Field(
        ...,
        description="text to be match in files content, context"
    )

    
    directory: str = Field(
        ...,
        description="require a relative or absolute directory path"
    )
    
    def handle(self) -> str:
        """delegating to FileSearchAgent"""
        task =  lr.Task(
        file_search_agent,
        interactive=False,
        restart=True
    )  
        
     
        prompt =f"find all files that match the query:{self.query} at directory: {self.directory}. Return only final results in the Content field." # Replace with your prompt
   
        result = task.run( prompt )  
        print( "final result ", result.content)
    
        return result.content