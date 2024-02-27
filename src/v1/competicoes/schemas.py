from pydantic import BaseModel

class CompeticaoBase(BaseModel):
    titulo: str


class CompeticaoRequest(CompeticaoBase):
    ...


class CompeticaoResponse(CompeticaoBase):
    id: int

    class Config:
        from_attributes = True
