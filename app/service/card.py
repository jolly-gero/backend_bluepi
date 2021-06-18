import random, ast
from .encrypt import GameKey

class cardManage:
    def __init__(self, GameKey):
        self.gameKey = GameKey

    def list_to_str(self, mylist):
        string = ",".join([str(item) for item in mylist])
        list_str = f'[{string}]'
        return list_str

    def str_to_list(self, mystr):
        str_list = ast.literal_eval(mystr)
        return str_list

    def create_suffleCard(self):
        list_card = []
  
        for index in range(1,7):
            item = {
                "num": index,
                "status": 0,
                "correct": 0
            }
            list_card.extend([item, item])

        random.shuffle(list_card)
        return list_card

    def createAllCard(self):
        createList = self.create_suffleCard()
        list_card = self.list_to_str(createList)
        key = self.gameKey.generate_key()
        encrypted = self.gameKey.encrypts(list_card, key)
        # print(type(list_card), list_card)
        # print("key >>",key)
        # print("encrypted >>", encrypted)

        return {
            "game_key" : key,
            "board_key": encrypted
        }

    def showAllCard(self, board_key, game_key):
        decrypted = self.gameKey.decrypted(board_key, game_key)
        listCards = self.str_to_list(decrypted)
        return listCards

    def stored(self, newList, key):
        list_card = self.list_to_str(newList)
        encrypted = self.gameKey.encrypts(list_card, key)
        return encrypted
