# agents/reasoning_agent.py

from utils.scoring import calculate_risk_score

def identify_dominant_driver(signals):
    if "limited" in signals.get("crew", ""):
        return "crew constraints"
    elif "storm" in signals.get("weather", ""):
        return "weather conditions"
    elif "delays" in signals.get("network", ""):
        return "network propagation"
    else:
        return "aircraft constraints"


def generate_candidate_actions(signals):
    """
    Simulates Tree-of-Thought branching
    """
    return [
        {"action": "reassign crew", "score": 0.85},
        {"action": "delay flights", "score": 0.65},
        {"action": "swap aircraft", "score": 0.55}
    ]


def run_reasoning(signals):
    risk_score = calculate_risk_score(signals)
    driver = identify_dominant_driver(signals)
    candidates = generate_candidate_actions(signals)

    return {
        "risk_score": risk_score,
        "driver": driver,
        "candidates": candidates
    }

