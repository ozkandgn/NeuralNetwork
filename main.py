import read
import weightPath
import tryNetwork
import calculate
import cloneNode
import train

def main():
    errorRate=0.001
    nodeWeight=read.Read()
    output=nodeWeight[-1][:]
    print("Lines=",nodeWeight)
    weight=weightPath.CreateWeightPath(nodeWeight)
    print("Weights=",weight)
    nodeWeight,result,difference=tryNetwork.Try(nodeWeight,weight,True)
    print("NewNodes=",nodeWeight)
    print("Results=",result)
    print("Differences=",difference)
    delta=cloneNode.CloneNodeValue(weight,0)#first delta must 0
    print(delta)
    delta,nodeS=calculate.CalculateDelta\
        (nodeWeight,weight,result,delta)
    print("Delta=",delta)

    while True:
        best=True
        for i in range(len(difference)):
            if difference[i] >= errorRate:
                best=False
        if best:
            print("\n\nTraining Successed!!!")
            break
        else:
            weight=train.Train(weight,delta)
            nodeWeight,result,difference=\
            tryNetwork.Try(nodeWeight,weight,False)
            
    nodeWeight,result,difference=tryNetwork.Try(nodeWeight,weight,True)
    print("NewNodes=",nodeWeight)
    print("Results=",result)
    print("Differences=",difference)
    
main()
