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

    results = main(n_simulators, num_decks)
    res = ". <br> ".join(results.split(". "))

    return render_template("form.html", result=res)


if __name__ == "__main__":
    app.run(debug=True)
