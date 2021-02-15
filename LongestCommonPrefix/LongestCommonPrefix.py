def longestCommonPrefix(self, strs: List[str]) -> str:
        #print(strs)
        countLetter = 0
        prefix = ""
        if len(strs) == 0:
            return ""
        for x in strs[0]:
            #print(x)
            isPrefix = 0
            for y in range(len(strs)-1):
                #print(strs[y+1][countLetter:10])                
                if((((strs[y+1][countLetter:210]).find(x)) == 0) and isPrefix == 0):
                    isPrefix = 0  
                else:
                    isPrefix = 1
                    #print("stop")
                #print(strs[y+1])
            if(isPrefix == 0):
                prefix += x
            else:
                return prefix
            countLetter += 1
        return prefix