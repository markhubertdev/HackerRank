 def isPalindrome(self, x: int) -> bool:
   
        def reverse(num):
            rev = 0
            while num > 0:
                rev = (10*rev) + num%10
                num //= 10
                
            return rev
        if x == reverse(x):
            return True
        else:
            return False
        