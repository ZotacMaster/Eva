""" here i need to make a python script that makes the claude_desktop_config.json file 
    in the correct location before/after the installation of claude desktop app.
""" 
import json 
from base import BaseAdapterClass

from utils.file_manager import ConfigFinder

class ClaudeAdapter(BaseAdapterClass):

    def __init__(self, agent_name):
        super().__init__(agent_name)

    def configure_mcp(self):
        """Configuration logic for claude desktop goes here"""
        cf = ConfigFinder("claude")
        config_path = cf.get_path()
        if not config_path:
            # ask user for permission to search the whole system
            config_path = cf.system_search()
        
        if config_path: 
            config = {
            "mcpServers": {
                "ContextManager": {
                    "command": "uv",
                    "args": [
                        "--directory",
                        config_path,
                        "run",
                        "context_mcp.py"
                    ]
                }
            }
        }
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=4)
        
        return super().configure_mcp()
    