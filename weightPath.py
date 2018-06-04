import numpy as np

def CreateWeightPath(nodeWeight):
    weight=[]
    for i in range(len(nodeWeight)-1):
        weight.append([])
        for j in range(len(nodeWeight[i])):
            weight[i].append([])
            for k in range(len(nodeWeight[i+1])-1):
                weight[i][j].append(np.random.random())
                if i==(len(nodeWeight)-2):
                    weight[i][j].append(np.random.random())    
    print("\nWeights Of Paths Is Created!!!")
    return weight
