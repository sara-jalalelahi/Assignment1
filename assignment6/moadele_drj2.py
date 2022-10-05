
import math
ans=0
def delta():
    return ans

a=int (input())
b=int (input())
c=int (input())
Δ=delta()
if Δ <0:
    print('javab nadard')
elif Δ==0:
    ans=(-1*b)/a
    print('javab=',ans)
    
elif Δ>0:
    x1=((-1*b)-math.sqrt(Δ))/(2*a)
    x2=((-1*b)+math.sqrt(Δ))/(2*a)
    print('javab1=',x1)
    print('javab2=',x2)