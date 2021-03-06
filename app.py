from flask import (
    Flask, render_template
)

import json, toml

WIDGETS = toml.load("data/widgets.toml")

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("status_line.html")

@app.route("/widgets/<widget_uuid>")
def widget(widget_uuid):
    return json.dumps({ "left": "timer:0h:25m:0s", "center": "text:!project", "right": "text:vibe mode" })
