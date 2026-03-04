import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a,b = np.array(a),np.array(b)
    dot_p = np.dot(a,b)
    norma = np.linalg.norm(a)
    normb = np.linalg.norm(b)
    if norma==0 or normb==0:
        return 0.0
    cos_sim = dot_p/(norma*normb)
    return cos_sim
    