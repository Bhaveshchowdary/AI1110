import numpy as num
from playsound import playsound
import math

arr = [0] * 20

finalarr = [0] * 20

index = 0
songindex = 0

while index<20:
    dummy = num.random.uniform(0, 20)
    dummy = math.floor(dummy)
    if arr[dummy] == 0 :
        finalarr[index] = dummy
        arr[dummy] = 1
        index+=1