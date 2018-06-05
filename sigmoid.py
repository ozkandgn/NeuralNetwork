def Sigmoid(x):
    try:
        x=round(x,10)
        return round(1/((1+round((2.718281828459**(round(-x,10))),10))),10)
              #number e ~= 2.718281828459
    except:
        pass
