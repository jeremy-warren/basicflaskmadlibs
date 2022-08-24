from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


@app.route("/")
def ask_questions():
    """base page asks the user to fill in prompt words"""

    prompts = story.prompts

    return render_template("questions.html", prompts=prompts)


@app.route("/completed")
def show_story():
    """"""
    finished_story = story.generate(request.args)
    return render_template("completed.html", text=finished_story)
