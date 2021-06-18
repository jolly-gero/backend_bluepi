from pydantic import BaseModel

class user(BaseModel):
    username: str
    best_score: int
    # game_key: str

class showUser(user):
    class Config():
        orm_mode =True

class gameIndex(BaseModel):
    idex: int
    vaule: int

class click(BaseModel):
    target: list
    username: str

class initUser(BaseModel):
    username: str
