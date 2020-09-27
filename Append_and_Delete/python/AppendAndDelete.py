import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
   
    getMin = (min(len(s), len(t)))
    
    firstDiffPosition = getMin
    
    for x in range(getMin):
        if (s[x] != t[x]):
            firstDiffPosition = x
            break
    steps = len(s) + len(t) - 2 * firstDiffPosition
    
    if  (k>= steps and (k-steps)%2 ==0) or k>= len(s)+len(t) or k == steps:
        return "Yes"
    else:
        return "No"