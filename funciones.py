def exhaustive_enumeration(target):
    answer = 0
    
    while answer**2 < target:
        answer += 1
    
    if answer**2 == target:
        print(f'{target} square root is {answer}')
    else:
        print(f'{target} does not have an exact square root')

def approach(target, epsilon):
    step = epsilon**2
    answer = 0.0
    iterations = 0

    while abs(answer**2 - target) >= epsilon and answer <= target:
        answer += step
        iterations += 1
    if abs(answer**2 - target) >= epsilon:
        print(f'no square root found for {target}')
    else:
        print(f'{target} square root is {answer}')

def binary_search(target, epsilon):
    low = 0.0
    tall = max(1.0, target)
    answer = (tall + low) / 2

    while abs(answer**2 - target) >= epsilon:
        print(f'low= {low}, tall= {tall}, answer={answer}')
        if answer**2 < target:
            low = answer
        else:
            tall = answer
        answer = (tall + low) / 2
    print(f'{target} square root is {answer}')

option = int(input('Choose an algorithm: \ (1) Exhaustive enumeration \ (2) Approach \(3) Binary search '))
def choose_number(option):
    print(f'You choose the option number {option}')
    number = (input(f'Choose a number: '))
    return


if option == 1:
    choose_number = choose_number(option)
    exhaustive_enumeration(choose_number)
elif option == 2:
    choose_number = choose_number(option)
    approach(choose_number,0.01)
elif option == 3:
    choose_number = choose_number(option)
    binary_search(choose_number, 0.01)
else:
    print(f'Please, choose the correct options')
