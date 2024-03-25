import numpy as np

def heads_or_tails():
    x = np.random.rand(1)
    if x > 0.3:
        return 'Tails'
    else:
        return 'Heads'

def heads_or_tails_v():
    x = np.random.rand(1)
    result = np.where(x > 0.3, 'Tails', 'Heads')
    return result[0]

def results():
    heads = {}
    tails = {}
    heads_value = 0
    tails_value = 0
    M = 1000
    
    while (heads_value + tails_value) != M:
        if heads_or_tails_v() == 'Heads':
            heads_value += 1
        else:
            tails_value += 1
    
    heads['Heads'] = heads_value/M
    tails['Tails'] = tails_value/M
    
    return heads, tails

results()