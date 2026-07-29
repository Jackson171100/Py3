from random import randint
# def add(a,b):
#     var1=a+b
#     print("hi")
#     return var1
# def multiply(a,b):
#     var1=a*b
#     return var1
# print(add(1,2))
# print(multiply(3,9))
def minecraft_oh_ya(seed):
    var1=(seed ^ 0x5deece66d) & (2**48-1)
    return var1
def next(seed,bits):
    var2=seed>>(48-bits)
    var3=(seed*0x5deece66d+11) & (2**48-1)
    return var2,var3
seed=minecraft_oh_ya(randint(0,111111111111111111111111111111111111111111111111111111111111111111111111))
var1,seed=next(seed,30)
print(var1)
var2,seed=next(seed,30)
print(var2)
var3,seed=next(seed,30)
print(var3)
var4,seed=next(seed,30)
print(var4)
def nextInt(n,seed):
    bits,seed=next(seed,31)
    val = bits % n
    while (bits - val + n -1) <0:
        bits,seed = next(seed,31)
        val = bits % n
    return val
print(nextInt(100,seed))