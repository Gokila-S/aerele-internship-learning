def process(data):
    result=[]
    for i in range(len(data)):
        if data[i]%2==0:
            result.append(data[i]*2)
    return result