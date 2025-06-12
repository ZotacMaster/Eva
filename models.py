from pydantic import BaseModel, Field
import uuid
import datetime
from typing import Dict, List, Optional, Any

#Temporary context data structure
class ContextData(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    content: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    source_agent: Optional[str] = None
    #TODO: Fix timestamp implementation
    #timestamp: datetime = Field(default_factory=datetime.utcnow)

class ContextQuery(BaseModel):
    query: Optional[str] = None
    source_agent: Optional[str] = None

class ContextResponse(BaseModel):
    contexts: List[ContextData]
    total: int
    has_more: bool

class HealthCheck(BaseModel):
    status: str
    #timestamp: datetime
    cache_connected: bool
    external_db_connected: bool

class AgentList(BaseModel):
    agent_name: str
    status: str
