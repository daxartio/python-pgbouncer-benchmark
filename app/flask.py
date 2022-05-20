from flask import Flask

from .common import do_something_sync

app = Flask(__name__)


@app.route("/test")
def hello_world():
    do_something_sync()
    return '{"Hello": "World"}'
