

## Objective

FileSearchAgent search through files to find content relevant matching. Agent as a tool (FileSearchTool) TBU agents.


1. **FileSearchAgent** - A specialized agent that:
   - Accepts search queries
   - Tool ListDirTool to explore directories
   - Tool ReadFileTool to examine file contents
   - Returns relevant files with explanations
   - Tool DoneTool to indicate completion

2. **FileSearchTool** - A tool wrapper that:
   - Takes other agents to delegated search tasks
   - Runs the FileSearchAgent 
   - Returns search results

## Files 

- `file_search_agent.py` -FileSearchAgent
- `search_tool.py` -  FileSearchTool wrapper
- `file_tools.py` - file manipulation tools (ListDirTool, ReadFileTool)
- `test.py` - test
- all scripts must be on the project folder
- Install all dependencies from pyproject.toml

-Set up configurations `.env` 

```bash
# .env file
OPENAI_API_KEY=your_api_key_here
OPENAI_API_BASE=https://your-api-base-url
OPENAI_CHAT_MODEL=gemini-2.5-flash  
```



```bash
# Run all tests
pytest test.py -v

# Run with a specific model
pytest test.py -v --model gemini-2.5-flash

# Run a specific test
pytest test.py::test_file_search_direct -v --model gemini-2.5-flash
```
