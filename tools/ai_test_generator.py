import requests
import json
import os

def generate_ai_test_cases(scenario):
    if (os.getenv("CI") == "true"):
        return ("AI generation skipped in CI")

    prompt = f"""
    You are a Senior QA Engineer.
    Generate:

    1. Test Scenario
    2. Preconditions
    3. Test Steps
    4. Expected Result
    5. Priority

    For:

    {scenario}

    Return clean text.
    """
    response = requests.post("http://localhost:11434/api/generate",
                             json={
                             "model":"llama3.2",
                             "prompt":prompt,
                             "stream":False
                             }
                             )
    result = response.json()
    return result["response"]