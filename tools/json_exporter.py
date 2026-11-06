import json
import os


def save_test_cases_json(test_cases):
    os.makedirs("outputs", exist_ok=True)
    with open("outputs/test_cases.json", "w",encoding="utf-8") as file:
        json.dump(test_cases, file, indent=4)