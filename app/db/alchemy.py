import sqlalchemy as sa
from sqlalchemy import orm

from app.db import interface

# Secondary adapter level
class Alchemy(interface.DB):
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
