import sys

appetizers = {
    'salad' : 0,
    'bread sticks' : 0,
    'cheese curds' : 0
}

entrees = {
    'street tacos' : 0,
    'new york strip' : 0,
    'surf & turf' : 0
}

desserts = {
    'mango coconut icecream' : 0,
    'banana split' : 0,
    'almond cake' : 0
}

beverages = {
    'modelos' : 0,
    'coffee' : 0,
    'pina colada' : 0
}

def exit_app():
    print('thank you for coming')
    sys.exit()

def menu():
    print('----------')
    print('appetizers')
    print('----------')
    for i in appetizers:
        print(i)
    
    print('----------')
    print('entrees')
    print('----------')
    for i in entrees:
        print(i)

    print('----------')
    print('desserts')
    print('----------')
    for i in desserts:
        print(i)

    print('----------')
    print('beverages')
    print('----------')
    for i in beverages:
        print(i)
    print('*********************************')

print('*********************************')
print('** welcome to the Snake Cafe!! **')
print('** Please see our menu below!! **')
print('**                             **')
print('** to leave page, type "quit"  **')
print('*********************************')

while True:
    enterance_anwser = input('Are you ready to see the menu?')
    print('before')
    if enterance_anwser == 'yes' or enterance_anwser ==  'y' or enterance_anwser == 'yea' or enterance_anwser ==  'ya':
        menu()
        break

while True:
    anwser = input('what would you like to order? ')
    if anwser == 'quit':
        exit_app()

    elif anwser in appetizers:
        appetizers[anwser] += 1 
        print(appetizers[anwser], anwser,'has been added to you order!')
    elif anwser in entrees:
        entrees[anwser] += 1
        print(appetizers[anwser], anwser,'has been added to you order!')
    elif anwser in desserts:
        desserts[anwser] += 1
        print(desserts[anwser], anwser,'has been added to you order!')
    elif anwser in beverages:
        beverages[anwser] += 1
        print(beverages[anwser], anwser,'has been added to you order!')
    else:
        print('Please input choice again')