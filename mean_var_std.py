import numpy as np

def calculate(lst : list[int]) -> dict: # function for all numpy calculations
    # initialize empty dictionary
    if len(lst) < 9: # if there are less than nine numbers in the list, raise ValueError
        raise ValueError("List must contain nine numbers.")
        
    arr = np.array(lst).reshape(3, 3) # create 3 x 3 numpy array
    results = {}

    # populate dictionary with all the calculations 
    results['mean'] = [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr.mean()]
    results['variance'] = [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), arr.var()]
    results['standard deviation'] = [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), arr.std()]
    results['max'] = [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr.max()]
    results['min'] = [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr.min()]
    results['sum'] = [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr.sum()]
    
    return results