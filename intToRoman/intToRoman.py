class Solution:
    def intToRoman(self, num: int) -> str:
        #print(num)
        numbers = [[1, "I"],[5,"V"],[10,"X"]]
        numbersTwo = [[1,"X"],[5, "L"],[10, "C"],[500,"D"],[1000, "M"]]
        numbersThree = [[1, "C"],[5,"D"],[10, "M"]]
        numLen = len(str(num))
        isMinusOne = 0
        minusNumber = 0
        numberString  = ""
        
        one = ""
        two = ""
        three = ""
        four = ""
        
        one = int(str(num)[-1])
        oneString = ""
        
        #case one digit or last digit
        if(numLen>0 and one != 0):
            #print(num)
            for x in range(3):
                checkNum = (numbers[x][0])
                if((checkNum - one) == 1):
                    isMinusOne = 1
                    minusNumber = checkNum
            if(isMinusOne == 0):
                if one >=5:
                    numberString += "V"
                    for x in range(one-5):
                        numberString += "I"
                    #return numberString
                    print("last "+numberString)
                if(one < 5):
                    numberString += "I"
                    for x in range(one - 1):
                        numberString += "I"
                    print("last "+numberString)  
                    #return numberString
            else:
                if(minusNumber == 10):
                    numberString += "IX"
                    #return numberString
                    print("last "+numberString)
                else:
                    numberString += "IV"
                    #return numberString
                    print("last "+numberString)
        if(numLen<2):
            return numberString
        else:
            oneString = numberString
            numberString = ""
            two = int(str(num)[-2])
            #print(two)
            isMinusOne = 0
            minusNumber = 0
            if(two != 0):
                #print(num)
                for x in range(3):
                    checkNum = (numbersTwo[x][0])
                    if((checkNum - two) == 1):
                        isMinusOne = 1
                        minusNumber = checkNum
                if(isMinusOne == 0):
                    if two >=5:
                        numberString += "L"
                        #print(two)
                        for x in range(two-5):

                            numberString += "X"
                        #return numberString
                        print("second "+numberString)

                    if(two < 5):
                        numberString += "X"
                        for x in range(two - 1):
                            #print(two)
                            numberString += "X"
                        print("second "+numberString)  
                        #return numberString

                else:
                    if(minusNumber == 10):
                        numberString += "XC"
                        #return numberString
                        print("second "+numberString)
                    else:
                        numberString += "XL"
                        #return numberString
                        print("second "+numberString)
        if(numLen<3):
            return (numberString+oneString)
        else:
            oneString = numberString+oneString
            numberString = ""
            three = int(str(num)[-3])
            #print(two)
            isMinusOne = 0
            minusNumber = 0
            if(three !=0):
                #print(num)
                for x in range(3):
                    checkNum = (numbersThree[x][0])
                    if((checkNum - three) == 1):
                        isMinusOne = 1
                        minusNumber = checkNum
                if(isMinusOne == 0):
                    if three >=5:
                        numberString += "D"
                        #print(two)
                        for x in range(three-5):

                            numberString += "C"
                        #return numberString
                        print("third "+numberString)

                    if(three < 5):
                        numberString += "C"
                        for x in range(three - 1):
                            #print(two)
                            numberString += "C"
                        print("third "+numberString)  
                        #return numberString

                else:
                    if(minusNumber == 10):
                        numberString += "CM"
                        #return numberString
                        print("third "+numberString)
                    else:
                        numberString += "CD"
                        #return numberString
                        print("third "+numberString)
        
        if(numLen<4):
            return (numberString+oneString)
        else:
            oneString = numberString+oneString
            numberString = ""
            four = int(str(num)[-4])
            #print(two)
            isMinusOne = 0
            minusNumber = 0
            numberString += "M"
            for x in range(four-1):
                numberString += "M"
            
            return (numberString+oneString)
                    
                
                
        