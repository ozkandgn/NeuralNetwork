def Read():
    biasValue=1
    inputs=[]
    outputs=[]
    try:
        text_file=open("testValues.txt", "r")
        lines=text_file.read().split('\n')
    except:
        return []
    for line in lines:
        line=line.split(':')
        tempLine=[int(i) for i in line[0].split(',')]
        tempLine.append(1)
        inputs.append(tempLine)
        tempLine=[int(i) for i in line[1].split(',')]
        outputs.append(tempLine)
    lines=[[]]
    lines[0].append(inputs[0])
    hiddenHeight= int(input('Please Enter Hidden Layers Height=\n'))
    tempInput=[]
    for i in range(hiddenHeight):
        tempInput.append(int(input('Please Enter Hidden Layers Length=\n')))
        tempLine=[0 for i in range(tempInput[i])]
        tempLine.append(1)
        tempInput[i]=tempLine        
        lines[0].append(tempLine)
    lines[0].append(outputs[0])
    for i in range(1,len(inputs)):
        lines.append([])
        lines[i].append(inputs[i])
        for j in range(hiddenHeight):
            lines[i].append(tempInput[j])
        lines[i].append(outputs[i])
    #print("L0",lines[0])
    #print("L1",lines[1])
    #print("\nRead Succesed!!!")
    return lines
