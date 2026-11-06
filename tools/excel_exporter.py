import os
import pandas as pd

def save_test_cases_excel(test_cases):

    os.makedirs("outputs",exist_ok=True)
    rows = []
    for tc in test_cases:
        rows.append(
            {

                "ID": tc["id"],
                "Scenario": tc["scenario"],
                "Precondition": tc["precondition"],
                "Steps": "\\n".join(tc["steps"]),
                "Expected Result": tc["expected_result"]
            }
        )

    df = pd.DataFrame(rows)
    df.to_excel("outputs/test_cases.xlsx",index=False)