import requests
import json

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
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    
    try:
        response = requests.post(f"{URL}?key={API_KEY}", headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"
    except (KeyError, IndexError):
        return "Error: Unexpected response format from API"

def run_debate(topic, rounds=3):
    optimist = "confident optimist"
    skeptic = "critical skeptic"
    debate = []
    
    # Round 1: Opening arguments
    opt_arg = generate_argument(topic, optimist)
    debate.append(("Optimist", opt_arg))
    skep_arg = generate_argument(topic, skeptic)
    debate.append(("Skeptic", skep_arg))
    
    # Subsequent rounds: Responses
    for _ in range(rounds - 1):
        opt_arg = generate_argument(topic, optimist, skep_arg)
        debate.append(("Optimist", opt_arg))
        skep_arg = generate_argument(topic, skeptic, opt_arg)
        debate.append(("Skeptic", skep_arg))
    
    return debate

if __name__ == "__main__":
    topic = input("Enter a debate topic: ")
    print(f"\nDebate Topic: {topic}\n")
    debate = run_debate(topic)
    for i, (speaker, argument) in enumerate(debate, 1):
        round_num = (i + 1) // 2
        print(f"Round {round_num} - {speaker}:")
        print(f"{argument}\n")