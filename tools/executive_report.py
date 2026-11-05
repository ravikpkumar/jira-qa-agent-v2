def generate_executive_report(story_id, summary,coverage_report, review_report):

    report = f"""
    =================================
    EXECUTIVE QA REPORT
    =================================

    Story:

    {story_id}

    Summary:

    {summary}

    Requirements:

    {coverage_report['requirements']}

    Generated Tests:

    {coverage_report['test_cases_count']}

    Coverage:

    {coverage_report['coverage']}%

    Review Status:

    {review_report['status']}

    Risk Level:

    {review_report['risk']}

    Recommendation:

    {review_report['recommendation']}

    =================================

    """

    return report