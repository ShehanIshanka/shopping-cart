from dataclasses import dataclass

import requests
from pydantic import BaseModel


@dataclass
class Request(BaseModel):
    pass


@dataclass
class Response(BaseModel):
    msg: str
    status: int = requests.codes.ok
