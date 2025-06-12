"""This is where the MCP server and its tools will be defined using FastMCP

    In order to get the required context from the severs or send the context to the severs
    an external proxy HTTP server will be hosted on a local port. The MCP tools will communicate
    with this HTTP server using httpx module to send and recieve context data.
"""
# External dependencies
import httpx
from typing import Union
from mcp.server.fastmcp import FastMCP

# Internal dependencies
from models import ContextData, ContextQuery, ContextResponse

mcp = FastMCP("Eva")
BASE_URL = "" # locally hosted HTTP proxy URL

@mcp.tool()
async def update_context(context: ContextData):
    """
    Updates stored context

    """
    async with httpx.AsyncClient() as client:
        response = client.post(
            f"{BASE_URL}/context/update",
            json=context.model_dump(mode="json"),
        )
    return response.json() if response.status_code == 200 else None


@mcp.tool()
async def fetch_context(session_id: str)-> str: 
    """
    Searches through the stored context and returns match(s)
    """
    #TODO: change the return type to a json object 
    pass

@mcp.tool()
def insert_context(context: ContextData):
    """
    Inserts context in the context database 
    """
    pass

@mcp.tool()
def test(data: ContextData, testItem: str) -> Union[ContextResponse, str]:
    """
    Simple testing tool to test core functionalities

    Args:
        data- Context data.
        testItem- Name of functionality to be tested.
    """
    pass