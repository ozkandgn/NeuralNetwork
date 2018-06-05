import tryNetwork

def Train(weight,delta):
    for i in range(len(delta)):
        for j in range(len(delta[i])):
            for k in range(len(delta[i][j])):
                weight[i][j][k]+=delta[i][j][k]
    return weight
    
