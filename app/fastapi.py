from fastapi import FastAPI

from .common import do_something_async, do_something_sync

app = FastAPI()


@app.get("/test-sync")
def get_test_sync():
    do_something_sync()
    return {"Hello": "World"}


@app.get("/test-async")
async def get_test_async():
    await do_something_async()
    return {"Hello": "World"}
