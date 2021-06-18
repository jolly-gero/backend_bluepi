from fastapi import APIRouter, Depends, status, HTTPException
from .. import schema
from sqlalchemy.orm import Session
from .. import dbconfig, models
from ..service.encrypt import GameKey 
from ..service.card import cardManage

router = APIRouter(
    prefix="/user",
    tags=["user"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

@router.post("/start", response_model= schema.showUser, status_code=status.HTTP_201_CREATED)
async def start(request : schema.initUser,db: Session = Depends(dbconfig.get_db)):

    if not request.username:
        raise HTTPException(status_code=404, detail="please enter your name")

    cards = cardManage(GameKey())
    cardDetail = cards.createAllCard()

    find_user = db.query(models.userData).filter(models.userData.username == request.username).first()
    if not find_user:
        new_user = models.userData(
            username = request.username, 
            best_score = 0,
            game_key = cardDetail["game_key"],
            board_key = cardDetail["board_key"]
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
  
    return find_user