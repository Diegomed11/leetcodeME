
n=3
def generateParenthesis(n):
    r = []
    def backtrak(p,a,b):
        if len(p)==2*n:
            r.append(p)
            return
        if a<n:
            backtrak(p+'(',a+1,b)
        if b<a:
            backtrak(p+')',a,b+1)
    backtrak('(',1,0)
    return r
print(generateParenthesis(n))

