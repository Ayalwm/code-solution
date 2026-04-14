from array import array
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr=[]
        previousRow=[]
        for i in range(numRows):
            if(i==0):
                previousRow=[1]
                arr.append(previousRow)
            elif (i==1):
                previousRow=[1,1]
                arr.append(previousRow)
            else:   
                Row = [0] * (i + 1)    
                for j in range(i):     
                    if(j==0 or j== i):   
                        Row[0]=1
                        Row[i]=1
                    else:
                        Row[j]=previousRow[j-1]+previousRow[j]
                previousRow = Row.copy()
                arr.append(previousRow)
        return arr