import sigmoid

def Try(nodeWeight,weight):
    result=[]
    difference=[]
    for i in range(1,len(nodeWeight)):
        if i==(len(nodeWeight)-1):
            for j in range(len(nodeWeight[i])):
                result.append([])
                difference.append([])
                for k in range(len(weight[i-1][j])):
                    if k==0:
                        result[j]=weight[i-1][k][j]*nodeWeight[i-1][k]
                    else:
                        result[j]+=weight[i-1][k][j]*nodeWeight[i-1][k]
                result[j]=sigmoid.Sigmoid(result[j])
                difference[j]=(nodeWeight[-1][j]-result[j])**2
        else:
            for j in range(len(nodeWeight[i])-1):
                for k in range(len(weight[i-1][j])):
                    if k==0:
                        nodeWeight[i][j]=weight[i-1][k][j]*nodeWeight[i-1][k]
                    else:
                        nodeWeight[i][j]+=weight[i-1][k][j]*nodeWeight[i-1][k]
                nodeWeight[i][j]=sigmoid.Sigmoid(nodeWeight[i][j])
    return nodeWeight,result,difference