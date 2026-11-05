def review_test_suite(coverage_report):
    coverage = coverage_report["coverage"]
    if coverage >= 100:
        status = "PASS"
        risk = "LOW"
        recommendation = "Requirement coverage is complete."
    elif coverage >= 80:
        status = "PASS"
        risk = "MEDIUM"
        recommendation = "Review missing tests."
    else:
        status = "FAIL"
        risk = "HIGH"
        recommendation = "Coverage insufficient."

    review = {"status": status, "risk":risk,"recommendation":recommendation
    }

    return review