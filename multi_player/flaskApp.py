from flask import Flask, request, render_template
from main import main

app = Flask(__name__)


@app.route("/")
def my_form():
    return render_template("form.html")


@app.route("/", methods=["POST"])
def get_result():
    n_simulators = int(request.form["n_simulators"])
    num_decks = int(request.form["num_decks"])
    num_players = int(request.form["num_players"])

    results = main(n_simulators, num_decks, num_players)
    return render_template("form.html", result=results)


if __name__ == "__main__":
    app.run(debug=True)
