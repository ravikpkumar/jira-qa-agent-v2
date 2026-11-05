def calculate_coverage(requirements, test_cases):
    requirement_count = len(requirements)
    test_cases_count = len(test_cases)
    coverage = (test_cases_count/requirement_count)*100
    return{
        "requirements": requirement_count,
        "test_cases_count": test_cases_count,
        "coverage": coverage
    }
