import numpy as np

def rmse(predictions, targets):
    pred = np.array(predictions)
    tar = np.array(targets)
    
    squared_diff = (pred - tar) ** 2
    mean_squared_diff = squared_diff.mean()
    
    rmse= np.sqrt(mean_squared_diff)
    return rmse