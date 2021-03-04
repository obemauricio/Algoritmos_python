target = int(input('Choose a number: '))
epsilon = 0.01
low = 0.0
tall = max(1.0, target)
answer = (tall + low) / 2

while abs(answer**2 - target) >= epsilon:
    print(f'low={low}, tall={tall}, answer={answer}')
    if answer**2 < target:
        low = answer
    else:
        tall = answer
    
    answer = (tall + low) / 2

print(f' {target} square root is {answer}')