
import pytest
from file_search_agent import run_file_search
from search_tool import FileSearchTool




def test_search_tool():

    tool = FileSearchTool(query="classical music", directory="myfiles")
    result = tool.handle()
    print (result)
    assert "mozart" in result.lower()
    assert len(result) > 20

def test_search_tool_no_results():

    tool = FileSearchTool(query="quantum physics astronomy", directory="myfiles")
    result = tool.handle()
    print (result)
    assert result.lower() == ""

# Run tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"])