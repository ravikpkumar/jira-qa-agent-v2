import os

def save_report(report):

    os.makedirs("outputs", exist_ok=True)
    with open("outputs/executive_report.txt","w",encoding="utf-8") as file:
        file.write(report)