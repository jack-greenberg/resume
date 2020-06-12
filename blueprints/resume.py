import json
from flask import Blueprint, render_template

resume_blueprint = Blueprint('resume', __name__, template_folder='templates', static_folder='static')

with open("resume.json") as f:
    resume = json.load(f)

@resume_blueprint.route("/")
def render_resume():
    with open("resume.json") as f:
        resume = json.load(f)
    return render_template("resume.j2", r=resume)
