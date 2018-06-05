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
    lines=[]
    lines.append(inputs[0])
    hiddenHeight= int(input('Please Enter Hidden Layers Height=\n'))
    for i in range(hiddenHeight):
        tempInput=int(input('Please Enter Hidden Layers Length=\n'))
        tempLine=[0 for i in range(tempInput)]
        tempLine.append(1)
        lines.append(tempLine)
    lines.append(outputs[0])
    print("\nRead Succesed!!!")
    return lines
