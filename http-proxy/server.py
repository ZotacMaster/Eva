from fastapi import FastAPI
import uvicorn
import argparse

from endpoints import fetch, update

server = FastAPI(title="http-proxy server", description="An http server to relay context info to the main db")

server.include_router(fetch.router)
server.include_router(update.router)

def main():
    parser = argparse.ArgumentParser(description="Run FastAPI JSON Server")
    parser.add_argument("--port", "-p", type=int, default=8000, help="Port to run the server on (default: 8000)")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="Host to run the server on (default: 127.0.0.1)")
    
    args = parser.parse_args()
    
    print(f"Starting FastAPI server on {args.host}:{args.port}")
    print(f"API documentation available at: http://{args.host}:{args.port}/docs")
    print(f"Alternative docs at: http://{args.host}:{args.port}/redoc")
    
    uvicorn.run(server, host=args.host, port=args.port)

if __name__ == "__main__": 
    main()