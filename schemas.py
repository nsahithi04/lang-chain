from typing import List

from pydantic import BaseModel, Field


class Source(BaseModel):
    """this is the schema for the sources used by the agent"""

    url: str = Field(description="the URL of the source")


class AgentResponse(BaseModel):
    """schema for the agent response with the answer and url"""

    answer: str = Field(description="the agents answer to the query")
    sources: List[Source] = Field(
        default_factory=List, description="List of sources used to generate the answer"
    )
