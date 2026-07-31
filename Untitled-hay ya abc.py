from math import sqrt
import time
import cubiomespi
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
# var1,seed=next(seed,30)
# print(var1)
# var2,seed=next(seed,30)
# print(var2)
# var3,seed=next(seed,30)
# print(var3)
# #var4,seed=next(seed,30)
#print(var4)
def nextInt(n,seed):
    bits,seed=next(seed,31)
    val = bits % n
    while (bits - val + n -1) <0:
        bits,seed = next(seed,31)
        val = bits % n
    return val
def distance_between_points(x1,y1, x2, y2):
    return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

#print(nextInt(100,seed))
for hay_ya in range(randint(0,1000000000),11111111111111111111111):

    gen=cubiomespi.Generator(cubiomespi.MCVersion.MC_1_20,hay_ya,cubiomespi.Dimension.DIM_OVERWORLD)
    spawn=cubiomespi.get_spawn_pos(gen)
    
    spawnx=spawn[0]
    spawnz=spawn[1]


    start = time.time()

    # strong_hold_saba_more_beef=cubiomespi.get_stronghold_pos(gen,100)
    # print(strong_hold_saba_more_beef)
    # print(time.time()-start)
    # close=1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111112324455645467676
    # for pos in strong_hold_saba_more_beef:
    #     posx=pos[0]
    #     posz=pos[1]

    #     distance=distance_between_points(spawnx,spawnz,posx,posz)
    #     if distance<close:
    #         close=distance
    # if close>(400):
    #     continue
    # print()
    # print(spawn)
    var67676789895838=cubiomespi.find_closest_structure(gen,cubiomespi.Structure.Ancient_City,spawnx,spawnz,1)
    if not var67676789895838:
        continue
    posx=var67676789895838[0]
    posz=var67676789895838[1]
    distince=distance_between_points(posx,posz,spawnx,spawnz)
    if distince>350:
        continue

    var67676789895838=cubiomespi.find_closest_structure(gen,cubiomespi.Structure.Mansion,spawnx,spawnz,1)
    if not var67676789895838:
        continue
    posx=var67676789895838[0]
    posz=var67676789895838[1]
    distince=distance_between_points(posx,posz,spawnx,spawnz)
    if distince>200:
        continue

  
    print(hay_ya)