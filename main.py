import read
import weightPath
import tryNetwork
import calculate
import cloneNode
import train

import time #time library

def main():
    errorRate=0.00001
    allNodes=read.Read()
    weight=weightPath.CreateWeightPath(allNodes[0])
    print(allNodes[0])
    allNodes[0],result,difference=tryNetwork.Try(allNodes[0],weight,True)
    delta=cloneNode.CloneNodeValue(weight,0)#first delta must 0
    delta,nodeS=calculate.CalculateDelta\
        (allNodes[0],weight,result,delta)
    print("NewNodes=",allNodes[0])
    print("Results=",result)
    print("Differences=",difference)
    end=False
    iteration=0
    firstTime=time.time()
    while not end:
        best=True
        for nodeWeight in allNodes:
            iteration+=1
            weight=train.Train(weight,delta)
            nodeWeight,result,difference=\
            tryNetwork.Try(nodeWeight,weight,False)
            delta,nodeS=calculate.CalculateDelta\
            (nodeWeight,weight,result,delta)
        for i in range(len(difference)):
            if difference[i] >= errorRate:
                best=False
        if best:
            end=True
            print("\n\nTraining Successed!!!\n")
            print("Iteration=",iteration)
            print("Time=",round(float(time.time()-firstTime),4),"\n")
            break
    end=""
    inputLen=len(allNodes[0][0])-1
    outputLen=len(allNodes[0][-1])
    end=input("Please Press Enter For Trying(leave for=after 'e' press enter)")
    while end!='e':
        for i in range(inputLen):
            nodeWeight[0][i]=float(input("Please Enter Input"))
        nodeWeight,result,difference=\
            tryNetwork.Try(nodeWeight,weight,False)
        print("Results=",result)
        end=input("Please Press Enter For Trying(leave for=after 'e' press enter)")
main()
