
def generate_test_cases(desc:str):
    tests = []
    for line in desc.splitlines():
        line = line.strip()
        if not line:
            continue

        if "Feature:" in line or "Acceptance Criteria:" in line:
            continue

        tests.append(f"Test:   {line}")


        # if line.startswith("1.") or line.startswith("2."):
        #     test_name = line.split(".", 1)[1].strip()
        #     tests.append(f"Test{test_name}")
    return tests        
