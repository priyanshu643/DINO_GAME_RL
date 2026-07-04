import random
import time
def object(elements, priority):
    result = random.choices(elements, weights=priority, k=1)[0]
    print(result)
    return(result)
def statments(results):
    base = 'result'
    if results == '_':
        print('ground')
    elif results == '1':
        print('obstetrical')

    choices = int(input("ENTER THE CHOICES\npress 0 to quit\nPress 1 to jump and press 2 to let it go: "))
    if choices == 0:
        print('good bye')
        state = False
    elif choices == 1 and results == '1':
        print('correct choice')
        pass
    elif choices == 2 and results == '_':
        print('correct choice')
        pass
    elif choices == 1 and results == '_':
        print('wrong choice')
        state = False
    elif choices == 2 and results == "1":
        print('You hit a wall')
        state = False
    else:
        print('Invald option')
        state = False
state = True

while state:
    ground_state = object(['_', '1'], [0.8, 0.08])
    statments(ground_state)