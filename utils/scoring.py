# utils/scoring.py

def calculate_risk_score(signals):
    score = 0

    if "storm" in signals.get("weather", ""):
        score += 0.3

    if "limited" in signals.get("crew", ""):
        score += 0.4

    if "delays" in signals.get("aircraft", ""):
        score += 0.1

    if "delays" in signals.get("network", ""):
        score += 0.2

    return round(score, 2)


def score_branch(option):
    """
    Simple scoring for ToT branches
    """
    return option.get("score", 0)
