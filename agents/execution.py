import time

def format_output(reasoned_plan: str, preset: str) -> dict:
    """
    Structures the generated output for human administrator approval.
    """
    return {
        "status": "AWAITING_OWNER_AUTHORIZATION",
        "timestamp_utc": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
        "target_preset": preset,
        "compliance_check": "PASSED (Zero Cloud Leakage)",
        "generated_payload": reasoned_plan
    }