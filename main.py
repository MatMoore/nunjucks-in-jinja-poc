import os

from flask import Flask, render_template
from flask.templating import Environment

app = Flask(__name__)


class RelEnvironment(Environment):
    """Override join_path() to enable relative template paths."""

    def join_path(self, template, parent):
        result = os.path.join(os.path.dirname(parent), template)
        return os.path.normpath(result)


app.jinja_environment = RelEnvironment


@app.route("/")
def hello_world():
    return render_template("index.html")
