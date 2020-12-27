    def reverse(self, x: int) -> int:
        def RepresentsInt(s):
            try: 
                s  = int(s)
                if abs(s) <= 2147483647:
                    return True
                else:
                    return False
            except ValueError:
                return False
        
        
        res = list(map(str, str(x)))
        res.reverse()
        s = ''.join(res)
        if s != "0":
            
            s = s.lstrip("0")
            if(s[-1] == "-"):
                s = s[-1]+s[:-1]        

        
        if RepresentsInt(s) == True:
            return s
        else:
            return 0