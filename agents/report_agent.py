import os
from tools.executive_report import generate_executive_report
from tools.file_writer import save_report

class ReportAgent:
    def process(self, state):

        report = generate_executive_report(state["story_id"],state["summary"],state["coverage"], 
                                           state["review"])
        save_report(report)
        state["report"] = report
        return state
