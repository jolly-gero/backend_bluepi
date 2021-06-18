from fastapi import APIRouter, Depends, status, HTTPException
from .. import schema
from sqlalchemy.orm import Session
from .. import dbconfig, models
from ..service.encrypt import GameKey 
from ..service.card import cardManage

router = APIRouter(
    prefix="/game",
    tags=["gameManage"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

@router.post("/flip", status_code=status.HTTP_200_OK)
async def flip(request : schema.click, db: Session = Depends(dbconfig.get_db)):
   
    find_user = db.query(models.userData).filter(models.userData.username == request.username).first()
    if not find_user:
        raise HTTPException(status_code=404, detail="user not found")

    cards = cardManage(GameKey())
    check = 0
    value = []

    listCards = cards.showAllCard(find_user.board_key, find_user.game_key)
    index_card = request.target
    if  len(index_card) == 2:
        c1 = listCards[index_card[0]-1]
        c2 = listCards[index_card[1]-1]

        print('calculate')
        if c2['correct'] == 1:
            check = 0
            value.append(listCards[index_card[0]-1]["num"])
        else:
            if c1['num'] == c2['num']:
                listCards[index_card[0]-1]['correct'] = 1
                listCards[index_card[1]-1]['correct'] = 1
                listCards[index_card[1]-1]['status'] = 1
                check =1
                value.extend([c1['num'], c2['num']])

            else:
                listCards[index_card[0]-1]['status'] = 0
                listCards[index_card[1]-1]['status'] = 0
                check = -1

    else:
        if listCards[index_card[0]-1]['status'] == 1 :
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="pick duplicate card")

        listCards[index_card[0]-1]['status'] = 1
        check = 0
        value.append(listCards[index_card[0]-1]["num"])
    

    stored = cards.stored(listCards, find_user.game_key)
    updateCard = db.query(models.userData).filter(models.userData.username == 
        request.username).update({"board_key" : stored})
    db.commit()
    
    return {
        "card" : value, 
        "correct": check,
        "listCards" : listCards
    }
