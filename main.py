from agents.requirement_agent import RequirementAgent
from agents.test_design_agent import TestDesignAgent
from agents.review_agent import ReviewAgent
from agents.report_agent import ReportAgent
from services.jira_client import get_issue
from services.jira_fields import get_field


# fields = get_field()
# for field in fields:
#     print(field["id"],">=", field["name"])

req_agent = RequirementAgent()
state = req_agent.process("DEMO-1")
# print("\nSTATE")
# for k,v in state.items():
#     print(f"{k}:{v}")


design_agent = TestDesignAgent()
state = design_agent.process(state)
print("\nAfter TestDesignAgent:")
print(len(state["test_cases"]))

review_agent = ReviewAgent()
state = review_agent.process(state)

report_agent = ReportAgent()
state = report_agent.process(state)

print("\nSTATE AFTER TEST DESIGN\n")
print("\nTotal Test Cases :", len(state["test_cases"]))
# print(state.keys())
print("\nCoverage:\n")
print(state["coverage"])
print("\nReview:\n")
print(state["review"])
print("\nREPORT\n")
print(state["report"])