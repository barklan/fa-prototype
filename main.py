import abc
from dataclasses import dataclass
import sqlalchemy as sa
from sqlalchemy import orm
import fastapi as fa

# Infrastructure level
app = fa.FastAPI()
engine = sa.create_engine("postgresql://postgres:postgres@localhost:5432/postgres", pool_pre_ping=True, future=True)  # type: ignore
SessionLocal = orm.sessionmaker(autocommit=False, autoflush=True, bind=engine, future=True)

def user_registry_dep():
    try:
        db = SessionLocal()
        yield UserRegistry(Alchemy(db))
    finally:
        db.close()

# Entity
@dataclass
class User:
    name: str
    email: str

# Secondary adapter level
class DBInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def new(self, user: User):
        raise NotImplementedError

    @property
    def entity_prop(self):
        raise NotImplementedError

# Secondary adapter level
class Alchemy(DBInterface):
    def __init__(self, session: orm.Session):
        self.session = session

    def new(self, user):
        self.session.execute(sa.insert(
            sa.table(
                "client",
                sa.column("name"),
                sa.column("email"),
            )).values(
                name=user.name,
                email=user.email
            )
        )
        self.session.commit()
        print("commited!")

# Entity use case
class UserRegistry():
    def __init__(self, db: DBInterface):
        self.db = db

    def new(self, name: str, email: str):
        # Validation here, probably.
        user = User(name, email)
        self.db.new(user)

# Primary adapter level
@app.get("/")
def register_new_user(
    registry: UserRegistry = fa.Depends(user_registry_dep),
    name: str = fa.Query(...),
    email: str = fa.Query(...),
):
    registry.new(name, email)
    return {name: email}
