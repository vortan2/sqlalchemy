from sqlalchemy import Integer, and_, func, insert, select, text, update
from sqlalchemy.orm import aliased

from src.database import async_engine, sync_engine, session_factory
from src.models import metadata_obj, workers_table, WorkersOrm


def get_123_sync():
    with sync_engine.connect() as conn:
        res = conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
        print(f"{res.first()=}")


async def get_123_async():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
        print(f"{res.first()=}")



def create_tables():
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)

def insert_data():
    with session_factory() as session:
        worker_bobr = WorkersOrm(username='Bobr')
        worker_volk = WorkersOrm(username='Volk')
        session.add_all([worker_volk, worker_bobr])
        session.commit()



























# def insert_workers():
#     with sync_engine.connect() as conn:
#         # stmt = """INSERT INTO workers (username) VALUES
#         #     ('Jack'),
#         #     ('Michael');"""
#         stmt = insert(workers_table).values(
#             [
#                 {"username": "Jack"},
#                 {"username": "Michael"},
#             ]
#         )
#         conn.execute((stmt))
#         conn.commit()