import numpy as np
from datetime import datetime

t0 = datetime.now()
arr=np.random.random(20)

print(arr)

for i in range(20):
    for j in range(i):
        if (arr[i]<arr[j]):
            s= arr[j]
            arr[j] = arr[i]
            arr[i] = s
            
    
t1 = datetime.now()

duration = t1 - t0

print("The minimum number is")
print(arr[0])
print("The processing last")
print(duration)

print("The list in descending order is")
print(arr)

