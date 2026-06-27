# agents/decision_agent.py

def select_best_action(candidates):
    if not candidates:
        return {"action": "no valid action", "score": 0}

    return max(candidates, key=lambda x: x["score"])


def generate_output(reasoning_result, best_action):
    return {
        "risk_score": reasoning_result["risk_score"],
        "dominant_driver": reasoning_result["driver"],
        "recommended_action": best_action["action"],
        "confidence": best_action["score"],
        "explanation": f"Selected {best_action['action']} based on highest score and dominant driver {reasoning_result['driver']}."
    }
