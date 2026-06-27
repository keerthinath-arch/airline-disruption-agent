# agents/critic.py

from utils.scoring import score_branch

def evaluate_and_prune(candidates, threshold=0.6):
    """
    Prunes weak branches (ToT pruning step)
    """
    valid = []

    for c in candidates:
        score = score_branch(c)
        if score >= threshold:
            valid.append(c)

    return valid
