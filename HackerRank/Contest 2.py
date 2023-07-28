def baseCheck(num, base):
    largestDigit = base - 1
    num = repr(num)[::-1] 
    for i in range(len(num)-1):
        if int(num[i]) <= largestDigit:
            continue
        elif int(num[i]) > largestDigit:
            replacement = int(num[i+1]) + 1
            num = num[:i+1] + str(replacement) + num[i+2:]
            num = num[:i] + "0" + num[(i + 1):]

    if int(num[-1]) > largestDigit:
        num = num + "1"
        num = num[:(-2)] + "0" + num[(-1):]
        
    num = str(num)[::-1] 
    
    return num

def binarySlicing(num):
    num = num[:1] + num[2:]
    return num
    
def binaryAdding(num):
    num = num[:1] + "b" + num[2:]
    return num
    

def findLastBinary(s):
    s = list(s)
    gigaBin = ""
    reverseGiga = ""
    search = "0"
    reverseSearch = "0"
    
    for i in range(len(s)):
        temp = ord(s[i])
        temp = int(binarySlicing(bin(temp)))
        temp = str(format(temp, "#08"))
        # print("gigaBin is", gigaBin)
        # print("temp is",temp)
        gigaBin = gigaBin + temp
        
    print("Final Binary", gigaBin)
    while True:
        print("LOOPED")
        counter = 0
        if search in gigaBin:
            print("search is",search)
            print("index is", gigaBin.find(search))
            deleteIndex = gigaBin.find(search)
            gigaBin = gigaBin[: deleteIndex] + gigaBin[deleteIndex + len(search):]
            print("New gigaBin is", gigaBin)
            
        
            reverseGiga = gigaBin[::-1]
            print("reverseGiga is",reverseGiga)
            reverseSearch = search[::-1]
            if int(reverseGiga.find(reverseSearch)) < 0:
                search = baseCheck(int(search)-1, 2)
                break
            print("reverseSearch is",reverseSearch)
            print("reversed index is", reverseGiga.find(reverseSearch))
            search = baseCheck(int(search)+1, 2)
            
        else:
            counter += 1
            
            reverseGiga = gigaBin[::-1]
            print("reverseGiga is",reverseGiga)
            reverseSearch = search[::-1]
            if int(reverseGiga.find(reverseSearch)) < 0:
                search = baseCheck(int(search)-1, 2)
                break
            print("reverseSearch is",reverseSearch)
            print("reversed index is", reverseGiga.find(reverseSearch))
            search = baseCheck(int(search)+1, 2)
        
        #Reverse Check
        if reverseSearch in reverseGiga:
            newdeleteIndex = reverseGiga.find(reverseSearch)
            reverseGiga = reverseGiga[: newdeleteIndex] + reverseGiga[newdeleteIndex + len(reverseSearch):]
            print("New reverseGiga is", reverseGiga)
            
          
        else:
            gigaBin = reverseGiga[::-1]
            search = reverseSearch[::-1]
            counter+=1
            
        if counter == 2:
            print("huh")
            search = baseCheck(int(search)-1, 2)
            break
        else: 
            continue
            
        print("gigaBin is", gigaBin)
        print(search)
    
    return int(search ,2)

    print(findLastBinary("Roses are red."))
