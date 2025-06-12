from fastapi import FastAPI
import uvicorn
import argparse

from .endpoints import fetch, update

# Testing imports
from .endpoints import testing

server = FastAPI(title="http-proxy server", description="An http server to relay context info to the main db")

server.include_router(fetch.router)
server.include_router(update.router)
server.include_router(testing.router)

def start_server(port: int = 8000, host: str = "127.0.0.1"):

    print(f"Starting FastAPI server on {host}:{port}")
    print(f"API documentation available at: http://{host}:{port}/docs")
    print(f"Alternative docs at: http://{host}:{port}/redoc")
    
    uvicorn.run(server, host=host, port=port)

if __name__ == "__main__": 
    start_server()