"""This is where the MCP server and its tools will be defined using FastMCP

    In order to get the required context from the severs or send the context to the severs
    an external proxy HTTP server will be hosted on a local port. The MCP tools will communicate
    with this HTTP server using httpx module to send and recieve context data.
"""
import httpx
from mcp.server.fastmcp import FastMCP

from models import ContextData, ContextQuery, ContextResponse

mcp = FastMCP("Eva")

@mcp.tool()
async def update_context(context: ContextData):
    pass

@mcp.tool()
async def fetch_context(session_id: str)-> str: 
    #TODO: change the return type to a json object 
    pass