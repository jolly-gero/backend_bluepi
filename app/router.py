from .routes import gameManage
from .routes import user

def init_routes(APP):
    APP.include_router(user.router)
    APP.include_router(gameManage.router)

