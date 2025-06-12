from abc import ABC, abstractmethod

class BaseAdapterClass(ABC):
    """
        The BaseAdapterClass defines a specific format for the making of the agent 
        specific adapters.
    """
    def __init__(self, agent_name: str):
        self.agent_name = agent_name
        # Add agent name to the list of agents connected

    @abstractmethod
    def configure_mcp(self):
        pass
