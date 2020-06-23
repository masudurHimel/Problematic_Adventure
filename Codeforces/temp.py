def QuestionsMarks(strArr):
    a = 0
    b =0
    for i in range(len(strArr)-1):
        for j in range(i,len(strArr)):
            if strArr[i].isnumeric() and strArr[j].isnumeric():
                x = int(strArr[i])
                y = int(strArr[j])
                if x+y ==10 :
                    
                    a,b = i,j

    target = strArr[a+1:b]
    c = target.count("?")
    print(c)
    if c==3:
        return "true"
    else:
        return "false"

# keep this function call here 
print(QuestionsMarks("9???1???9??1???9"))