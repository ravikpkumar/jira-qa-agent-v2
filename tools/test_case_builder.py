from tools.detailed_test_builder import build_detailed_steps

def build_test_case(test_names:str):
    test_cases = []
    for index, test_name in enumerate(test_names,start=1):
        scenario = test_name.replace("Test:   ","")
        expected = get_expected_result(scenario)
        steps = build_detailed_steps(scenario)

        test_case = {
            "id": f"TC{index:03}",
            "scenario": scenario,
            "precondition": "Valid test environment available",
            "steps":steps,
            "expected_result": expected                  
        }
        test_cases.append(test_case)    
    return test_cases


def get_expected_result(scenario):
    mapping ={
        "Valid Login": "User should login successfully and receive JWT token.",
        "Invalid Login": "System should reject invalid credentials.",
        "JWT Validation": "Token should be generated and validated successfully.",
        "Session Timeout": "Session should expire after configured timeout.",
        "Rate Limiting": "System should block excessive requests."
    }
    return mapping.get(scenario, "Expected behaviour should be verified.")