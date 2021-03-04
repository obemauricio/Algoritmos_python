target = int(input('Choose an interger: '))
answer = 0

while answer**2 < target:
    print(answer)
    answer += 1
    
if answer**2 == target:
    print(f'The square root of {target} is {answer}')
else:
    print(f'{target} does not have an exact square root')