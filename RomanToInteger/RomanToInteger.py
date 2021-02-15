
    def romanToInt(self, s: str) -> int:
        numDict = [["I",1], ["V",5], ["X",10], ["L",50], ["C",100], ["D",500], ["M",1000]]
        #collectNum = []
        result = 0
        append = 0
        count = 0
        for x in s:
            #print(x)
            for el in numDict:
                if(x in el):
                    if(result == 0):
                        result = el[1]
                        append = el[1]
                        
                    else:
                        if(el[1]<= append):
                            result += el[1]
                            append = el[1]
                            
                        else:
                            if(count < 2):
                                result = (el[1]-append)                            
                            else:
                                result = result + (el[1]-append)-append
                                append = el[1]
                                
                    count += 1
        return result
                    
        
                    
        