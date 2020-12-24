def longestPalindrome(self, s: str) -> str:
        #print(s)
        sLen = len(s)
        maxLen = 0
        start = 0
        
        for i in range(1, sLen):
            
            low = i - 1
            high = i
            
            #print(low)
            #print(high)
            #print(s[low])
            #print(s[high])
            while low >= 0 and high < sLen and s[low] == s[high]:
                #print(s[low])
                #print(s[high])
                if high - low + 1 > maxLen:
                    start = low
                    maxLen = high - low + 1
                low -= 1
                high += 1
            
            low = i - 1
            high = i + 1
            
            while low >= 0 and high < sLen and s[low] == s[high]:
                #print(s[low])
                #print(s[high])
                if high - low + 1 > maxLen:
                    start = low
                    maxLen = high - low + 1
                low -= 1
                high += 1
        if(maxLen == 0):
            return s[0]
        else:
            return(s[start:start + maxLen])