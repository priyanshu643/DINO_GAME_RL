import random
import time
def object(elements, priority):
    result = random.choices(elements, weights=priority, k=1)[0]
    print(result)
    return(result)
state = True

while state:
    object(['_', '1'], [0.85, 0.05])
    #print(results)
    time.sleep(0.2)