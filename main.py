import read
import weightPath
import tryNetwork

def main():
    nodeWeight=read.Read()
    output=nodeWeight[-1][:]
    print("Lines=",nodeWeight)
    weight=weightPath.CreateWeightPath(nodeWeight)
    print("Weights=",weight)
    nodeWeight,result,difference=tryNetwork.Try(nodeWeight,weight)
    print("NewNodes",nodeWeight)
    print("Results",result)
    print("Differences",difference)
    
main()
