def convert(self, s: str, numRows: int) -> str:
        #print(s)
        #print(numRows)
        arr = [""]*numRows
        
            
        #print(arr)
        rowCount = 1
        down = 1
        #up = 0
        if(numRows > 1):
            for x in s:
                if(rowCount<=numRows and down == 1):
                    #print(x + ' '+str(rowCount))
                    arr[rowCount-1] = arr[rowCount-1]+x
                    if rowCount == numRows:
                        down = 0
                        rowCount -= 1
                    else:
                        rowCount += 1
                elif(rowCount >= 1 and down == 0):
                    #print(x + ' '+str(rowCount))
                    arr[rowCount-1] = arr[rowCount-1]+x
                    if(rowCount == 1):
                        down = 1
                        rowCount += 1
                    else:
                        rowCount -= 1
            return(''.join(arr))
        else:
            return(s)