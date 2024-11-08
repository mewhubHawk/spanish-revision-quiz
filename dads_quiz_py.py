from flask import Flask, render_template, jsonify
import os
import json

app = Flask(__name__)

QUIZ_DIR = "quizzes"
HIGH_SCORE_FILE = "high_scores.json"

def load_high_scores():
    """Load high scores from the JSON file."""
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as file:
            return json.load(file)
    else:
        return {}

def save_high_scores(scores):
    """Save high scores to the JSON file."""
    with open(HIGH_SCORE_FILE, "w") as file:
        json.dump(scores, file)

@app.route("/save_responses/<quiz_name>", methods=["POST"])
def save_responses(quiz_name):
    responses = request.json.get("responses", [])
    filename = f"data/{quiz_name}_responses.json"

    if os.path.exists(filename):
        with open(filename, "r") as file:
            existing_data = json.load(file)
    else:
        existing_data = []

    existing_data.extend(responses)

    with open(filename, "w") as file:
        json.dump(existing_data, file, indent=4)

    return jsonify({"message": "Responses saved successfully!"})

@app.route("/load_incorrect_questions/<quiz_name>")
def load_incorrect_questions(quiz_name):
    filename = f"data/{quiz_name}_responses.json"
    
    if os.path.exists(filename):
        with open(filename, "r") as file:
            responses = json.load(file)
    else:
        return jsonify({"incorrect_questions": []})

    incorrect_questions = [resp for resp in responses if not resp["correct"]]

    return jsonify({"incorrect_questions": incorrect_questions})

@app.route("/")
def home():
    """Serve the main HTML page."""
    return render_template("index.html")

@app.route("/get_quizzes")
def get_quizzes():
    """List available quiz files."""
    quizzes = [f.split(".")[0] for f in os.listdir(QUIZ_DIR) if f.endswith(".json")]
    return jsonify(quizzes)

@app.route("/load_quiz/<quiz_name>")
def load_quiz(quiz_name):
    """Load the selected quiz JSON data."""
    quiz_path = os.path.join(QUIZ_DIR, f"{quiz_name}.json")
    if os.path.exists(quiz_path):
        with open(quiz_path, "r") as file:
            quiz_data = json.load(file)
        return jsonify(quiz_data)
    else:
        return jsonify({"error": "Quiz not found"}), 404

@app.route("/get_high_score/<quiz_name>")
def get_high_score(quiz_name):
    """Return the high score for the specified quiz."""
    high_scores = load_high_scores()
    score = high_scores.get(quiz_name, 0)
    return jsonify({"high_score": score})

@app.route("/update_high_scores/<quiz_name>", methods=["POST"])
def update_high_scores(quiz_name, new_score):
    """Update the high score if the new score is higher."""
    
    high_scores = load_high_scores();

    # Update the high score only if the new score is greater
    if new_score > high_scores.get(quiz_name, 0):
        high_scores[quiz_name] = new_score
        save_high_scores(high_scores)
        return jsonify({"message": "High score updated!", "high_score": new_score})
    else:
        return jsonify({"message": "No update needed", "high_score": high_scores[quiz_name]})

if __name__ == "__main__":
    app.run(debug=True)
