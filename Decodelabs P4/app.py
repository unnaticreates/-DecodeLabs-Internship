from flask import Flask, render_template, request
from questions import quiz_questions

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        score = 0

        for i, q in enumerate(quiz_questions):
            answer = request.form.get(f"q{i}")

            if answer and answer.lower() == q["answer"].lower():
                score += 1

        return render_template(
            "result.html",
            score=score,
            total=len(quiz_questions)
        )

    return render_template(
        "index.html",
        questions=quiz_questions
    )


if __name__ == "__main__":
    app.run(debug=True)