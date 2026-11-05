def build_detailed_steps(scenario):

    mapping = {

        "Valid Login": [
            "Navigate to Login API",
            "Provide valid username",
            "Provide valid password",
            "Submit request"
        ],

        "Invalid Login": [
            "Navigate to Login API",
            "Provide invalid username",
            "Provide invalid password",
            "Submit request"
        ],

        "JWT Validation": [
            "Perform successful login",
            "Capture JWT token",
            "Validate token structure",
            "Validate expiration"
        ],

        "Session Timeout": [
            "Login successfully",
            "Remain idle",
            "Wait for timeout",
            "Verify session expiry"
        ],

        "Rate Limiting": [
            "Send multiple login requests",
            "Exceed threshold",
            "Verify rate-limit response"
        ]
    }

    return mapping.get(
        scenario,
        ["Verify functionality"]
    )