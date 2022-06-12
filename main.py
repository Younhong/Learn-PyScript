import math
import numpy as np
import random

output_el = Element('output').element
# console.log(output_el)

# name = 'Brad'
# print(name)

# def getSum(x, y):
#     return x + y
        
# sum = getSum(5, 5)

# console.log(sum)
# pyscript.write('output', sum)
        
# pyscript.write('output2', math.sqrt(10))

arr = np.array([22, 58, 57, 87, 34, 5])

# pyscript.write('output', f"{arr}")
output_el.innerHTML = f"{arr}"

def shuffle_array(*args):
    # Shuffle
    shuffled = sorted(arr, key=lambda k: random.random())
    # pyscript.write('output', shuffled)
    output_el.innerHTML = shuffled

