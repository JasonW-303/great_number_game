from flask import Flask, render_template, request, redirect, session
from pprint import pprint
import random

number = random.randint(1, 100)
print(number)

app = Flask(__name__)
app.secret_key = "abcd-1234"


@app.get("/")
def number_game():

    return render_template("index.html")


@app.post("/process")
def process():
    print("USER'S GUESS: ", request.form["user_guess"])
    user_guess_str = request.form["user_guess"]
    user_guess_int = int(user_guess_str)
    session["user_guess"] = user_guess_int

    if user_guess_int > number:
        return redirect("/results/high")
    elif user_guess_int < number:
        return redirect("/results/low")
    else:
        return redirect("/results/correct")


@app.get("/results/high")
def results_high():
    return render_template("results_high.html")


@app.get("/results/low")
def results_low():
    return render_template("results_low.html")


@app.get("/results/correct")
def results_correct():
    return render_template("results_correct.html")


@app.post("/destroy_session")
def destroy_session():
    session.clear()
    global number
    number = None
    number = random.randint(1, 100)
    print(number)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
