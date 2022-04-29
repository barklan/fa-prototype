import sqlalchemy as sa
from sqlalchemy import orm

engine = sa.create_engine("postgresql://postgres:postgres@localhost:5432/postgres", pool_pre_ping=True, future=True)  # type: ignore
SessionLocal = orm.sessionmaker(autocommit=False, autoflush=True, bind=engine, future=True)
