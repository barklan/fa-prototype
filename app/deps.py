from app.db import engine
from app.users import registry
from app.db import alchemy

def user_registry_dep():
    try:
        db = engine.SessionLocal()
        yield registry.Users(alchemy.Alchemy(db))
    finally:
        db.close()
