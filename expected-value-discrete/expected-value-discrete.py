import numpy as np
from typing import List

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.array(x)
    p = np.array(p)
    if np.any(p<0) or np.any(p>1):
        raise ValueError("probability cannot be less than zero or greater than one ")
    if not np.isclose(np.sum(p), 1.0):
        raise ValueError("Probabilities must sum to 1")
    if len(x)==len(p):
        sum_val = np.sum(np.array(x)*np.array(p))
        return sum_val
    else:
        raise ValueError("leghth of proabability array and observed value should be same")
