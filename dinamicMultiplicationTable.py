def multiply():
    res = base * inicial
    print(f'{base} * {inicial} = {res}')

def cond():
    global inicial
    if (inicial < final):
        while inicial < final:
            multiply()
            inicial += step
    else:
        while inicial > final:
            multiply()
            inicial -= step

def divline():
    print("___________________________________")

divline()
print("DINAMIC MUTIPLICATION TABLE")
print("    .......          ")
option = input('CHOOSE BETWEEN: \n 1 - To choose how many times it will execute the multiply operation  \n 2 - Type the inicial and final numbers \n The chosen one: ')
while (option != "1" and option != "2"):
    divline()
    option = input('\n TRY AGAIN \n CHOOSE BETWEEN: \n 1 - To choose how many times it will execute the multiply operation  \n 2 - Type the inicial and final numbers \n The chosen one: ')

divline()
base = int(input('Base Number: '))
inicial = int(input('Inicial Number: '))

if(option == "1"):
    qntd = int(input('How many times: '))
    step = int(input('Steps by each interaction: '))
    final = inicial + (qntd * step)
    divline()
    print("Result: ")
    cond()

else:
    final = int(input('Last Number: '))
    step = int(input('Steps by each interaction: '))
    divline()
    print("Result: ")
    cond()

key = input("press any key to quit...")