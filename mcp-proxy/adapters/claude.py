""" here i need to make a python script that makes the claude_desktop_config.json file 
    in the correct location before the installation of claude desktop app.
""" 
from base import BaseAdapterClass

class ClaudeAdapter(BaseAdapterClass):

    def __init__(self, agent_name):
        super().__init__(agent_name)

    def configure_mcp(self):
        """Configuration logic for claude desktop goes here"""
        return super().configure_mcp()
