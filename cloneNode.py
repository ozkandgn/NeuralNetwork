def CloneNodeEmpty(node):
    newNode=[]
    try:
        for i in node:
            newNode.append(CloneNodeEmpty(i))
        return newNode
    except:
        return []
    
def CloneNodeValue(node,value):
    newNode=[]
    try:
        for i in node:
            newNode.append(CloneNodeValue(i,value))
        return newNode
    except:
        return value
