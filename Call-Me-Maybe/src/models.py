from pydantic import BaseModel
from typing import Dict, Any, Optional


class Parameter(BaseModel):
    type: str


class FunctionDefinition(BaseModel):
    name: str
    description: str
    parameters: Dict[str, Parameter]
    returns: Dict[str, str]


class FunctionCallResult(BaseModel):
    prompt: Optional[str] = None
    name: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
