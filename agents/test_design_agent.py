from tools.test_generator import generate_test_cases
from tools.test_case_builder import build_test_case
from tools.ai_test_generator import generate_ai_test_cases

class TestDesignAgent:
    def process(self, state):

        requirements = state["requirements"]
        print("\nRequirements:\n")
        print(requirements)

        tests = generate_test_cases(requirements)
        print("\nGenerated Tests:\n")
        print(tests)

        test_cases = build_test_case(tests)
        print("\nGenerated Test Cases:\n")
        print(test_cases)

        for tc in test_cases:
            print(f"\nGenerating AI design for {tc['scenario']}")
            ai_design = generate_ai_test_cases(tc['scenario'])
            tc["ai_test_design"] = ai_design        

        state["test_cases"] = test_cases
        print("\nBefore Return - Stored Test Cases:")
        print("\nStored Test Cases:",len(test_cases))

        return state