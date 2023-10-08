from pydantic import BaseModel


class Request(BaseModel):
    pass


class Response(BaseModel):
    pass


class HttpResponse(Response):
    msg: str
    status: int
