import cloneNode

def CalculateDelta(nodeWeight,weight,result,delta):
    learningRate=0.25
    momentum=0.9
    nodeS=cloneNode.CloneNodeEmpty(nodeWeight)
    for i in reversed(range(1,len(nodeWeight))):
        if i==len(nodeWeight)-1:
            for j in range(len(nodeWeight[i])):
                nodeS[i][j]=(nodeWeight[i][j]-result[j])\
                                *result[j]*(1-result[j])
            for j in range(len(nodeWeight[i-1])):
                for k in range(len(weight[i-1][j])):
                    delta[i-1][j][k]=learningRate*nodeS[i][k]\
                        *nodeWeight[i-1][j]+momentum*delta[i-1][j][k]
        else:
            for j in range(len(nodeWeight[i])):
                for k in range(len(weight[i][j])):
                    if k==0:
                        nodeS[i][j]=nodeS[i+1][k]*weight[i][j][k]\
                            *nodeWeight[i][j]*(1-nodeWeight[i][j])
                    else:
                        nodeS[i][j]+=nodeS[i+1][k]*weight[i][j][k]\
                            *nodeWeight[i][j]*(1-nodeWeight[i][j])
            for j in range(len(nodeWeight[i-1])):
                for k in range(len(weight[i-1][j])):
                    delta[i-1][j][k]=learningRate*nodeS[i][k]\
                        *nodeWeight[i-1][j]+momentum*delta[i-1][j][k]
    #print("\nDelta Calculate Successed!!!")
    return delta,nodeS
