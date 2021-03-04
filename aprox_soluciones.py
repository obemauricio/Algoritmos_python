target = int(input('Choose a number: '))
epsilon = 0.01
step = epsilon**2
answer = 0.0

while abs(answer**2 - target) >= epsilon and answer <= target:
    answer += step

if abs(answer**2 - target) >= epsilon:
    print(f'{target} square root not found')
else:
    print(f'Square root of {target} is {answer}')