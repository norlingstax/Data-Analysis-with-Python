import numpy as np

def calculate(list):
    if (len(list) > 9) or (len(list) < 9):
        raise ValueError('List must contain nine numbers.') 

    arr = np.array(list)
    arr = arr.reshape((3, 3))

    mean0 = arr.mean(axis = 0).tolist()
    mean1 = arr.mean(axis = 1).tolist()
    mean = arr.mean().tolist()

    var0 = arr.var(axis = 0).tolist()
    var1 = arr.var(axis = 1).tolist()
    var = arr.var().tolist()

    std0 = arr.std(axis = 0).tolist()
    std1 = arr.std(axis = 1).tolist()
    std = arr.std().tolist()

    maxx0 = arr.max(axis = 0).tolist()
    maxx1 = arr.max(axis = 1).tolist()
    maxx = arr.max().tolist()

    minn0 = arr.min(axis = 0).tolist()
    minn1 = arr.min(axis = 1).tolist()
    minn = arr.min().tolist()

    summ0 = arr.sum(axis = 0).tolist()
    summ1 = arr.sum(axis = 1).tolist()
    summ = arr.sum().tolist()
    
    calculations = {'mean':[mean0, mean1, mean],
    'variance':[var0, var1, var], 
    'standard deviation':[std0, std1, std], 
    'max':[maxx0, maxx1, maxx], 
    'min':[minn0, minn1, minn], 
    'sum':[summ0,summ1,summ]}
    
    return calculations