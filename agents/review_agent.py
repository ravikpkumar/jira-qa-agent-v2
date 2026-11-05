from tools.coverage_analyzer import calculate_coverage
from tools.reviewer import review_test_suite

class ReviewAgent:
    def process(self, state):
        requirements = []
        for line in (state["requirements"].splitlines()):
            line = line.strip()
            if not line:
                continue
            if "Feature:" in line or "Acceptance Criteria:" in line:
                continue
            requirements.append(line)
            coverage = calculate_coverage(requirements, state["test_cases"])
            review = review_test_suite(coverage)
            
        state["coverage"] = coverage
        state["review"] = review

        return state
                
