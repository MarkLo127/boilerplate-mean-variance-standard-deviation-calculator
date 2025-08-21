import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array(lst).reshape(3, 3)
    
    calculations = {
        'mean': [
            np.mean(arr, axis=0).tolist(),   # axis 0 (columns)
            np.mean(arr, axis=1).tolist(),   # axis 1 (rows)
            np.mean(arr).item()              # flattened
        ],
        'variance': [
            np.var(arr, axis=0).tolist(),
            np.var(arr, axis=1).tolist(),
            np.var(arr).item()
        ],
        'standard deviation': [
            np.std(arr, axis=0).tolist(),
            np.std(arr, axis=1).tolist(),
            np.std(arr).item()
        ],
        'max': [
            np.max(arr, axis=0).tolist(),
            np.max(arr, axis=1).tolist(),
            np.max(arr).item()
        ],
        'min': [
            np.min(arr, axis=0).tolist(),
            np.min(arr, axis=1).tolist(),
            np.min(arr).item()
        ],
        'sum': [
            np.sum(arr, axis=0).tolist(),
            np.sum(arr, axis=1).tolist(),
            np.sum(arr).item()
        ]
    }
    
    return calculations

# 範例
# print(calculate([0,1,2,3,4,5,6,7,8]))
