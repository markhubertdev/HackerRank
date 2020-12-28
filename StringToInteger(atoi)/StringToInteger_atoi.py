def myAtoi(self, s: str) -> int:
        
        def is_int(n):
            try:
                int(n)
            except ValueError:
                return False
            return True
        
        result  = ""
        s = s.lstrip()
        if(s=="" or s=="+" or s=="-"):
            result = "0"
            return int(result)
        
        for x in range(len(s)):
            if((s[x] == "+" or s[x]=="-") and x == 0 ):
                
                result = s[x].replace("+", "")
            else:
                if(is_int(s[x]) == True):
                    result = result + s[x]
                else:
                    
                    if(result == "" or result=="-"):
                        result = "0"
                    break
        if(float(result)>2147483647):
            result = 2147483647
        elif(float(result)<-2147483648):
            result = -2147483648
            
        return int(result)