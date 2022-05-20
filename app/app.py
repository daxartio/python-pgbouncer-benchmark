import asyncio

from .common import do_something_async, do_something_sync


def main():
    print(do_something_sync())
    print(asyncio.run(do_something_async()))
