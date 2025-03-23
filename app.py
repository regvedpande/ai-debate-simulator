from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

# Gemini API setup
API_KEY = ""
URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

def generate_argument(topic, persona, previous_argument=None):
    headers = {"Content-Type": "application/json"}
    if previous_argument:
        prompt = f"You are a {persona} AI. Respond concisely (50-100 words) to this argument about '{topic}': '{previous_argument}'"
    else:
        prompt = f"You are a {persona} AI. Provide a concise argument (50-100 words) about: {topic}"
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    try:
        response = requests.post(f"{URL}?key={API_KEY}", headers=headers, json=data)
        response.raise_for_status()
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return "Error: Could not generate argument"

def run_debate(topic, rounds=3):
    optimist = "confident optimist"
    skeptic = "critical skeptic"
    debate = []
    opt_arg = generate_argument(topic, optimist)
    debate.append(("Optimist", opt_arg))
    skep_arg = generate_argument(topic, skeptic)
    debate.append(("Skeptic", skep_arg))
    for _ in range(rounds - 1):
        opt_arg = generate_argument(topic, optimist, skep_arg)
        debate.append(("Optimist", opt_arg))
        skep_arg = generate_argument(topic, skeptic, opt_arg)
        debate.append(("Skeptic", skep_arg))
    return debate

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        topic = request.form["topic"]
        debate = run_debate(topic)
        return render_template("index.html", topic=topic, debate=debate)
    return render_template("index.html", topic=None, debate=None)

if __name__ == "__main__":
    app.run(debug=True)