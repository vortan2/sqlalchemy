import asyncio
from typing import Annotated

from sqlalchemy import String, create_engine, text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from config import settings

sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    # pool_size=5,
    # max_overflow=10,
)

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,
)
with engine.connect() as conn:
    res = conn.execute(text('SELECT 1,2,3 union select 4,5,6'))
    print(f'{res.first()=}')

session_factory = sessionmaker(sync_engine)
async_session_factory = sessionmaker(async_engine)

str_200 = Annotated[str, 200]

class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(200)

    }