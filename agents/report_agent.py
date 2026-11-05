from tools.executive_report import generate_executive_report
class ReportAgent:
    def process(self, state):

        report = generate_executive_report(state["story_id"],state["summary"],state["coverage"], 
                                           state["review"])
        state["report"] = report
        return state
