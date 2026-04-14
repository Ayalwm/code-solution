class Solution:
    d = {}
    def fib(self, n: int) -> int:
        if(n==0):
            return 0
        if(n==1):
            return 1
        if(n-1 in self.d and n-2 in self.d):
            x = self.d[n-1] + self.d[n-2]
            self.d[n] = x
            return x
        elif(n-1 in self.d):
            x = self.d[n-1] + self.fib(n-2)
            self.d[n] = x
            return x
        elif(n-2 in self.d):
            x = self.fib(n-1) + self.d[n-2]
            self.d[n] = x
            return x
        else:
            x = self.fib(n-1) + self.fib(n-2)
            self.d[n] = x
            return x