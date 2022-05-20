import asyncio
import os

from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool

database_url = os.environ["DATABASE_URL"]
sql = "select pg_sleep(0.2)"

engine = create_engine("postgresql+psycopg2://" + database_url, poolclass=NullPool)
async_engine = create_async_engine(
    "postgresql+asyncpg://" + database_url, poolclass=NullPool
)


def do_something_sync():
    with engine.connect() as conn:
        return list(conn.execute(sql))


async def do_something_async():
    async with async_engine.connect() as conn:
        return list(await conn.execute(text(sql)))
