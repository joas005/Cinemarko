import os
import time
os.system('cls' if os.name == 'nt' else 'clear')

# Definitions -
availibleRooms = ["1", "2", "3", "4", "5"]
availibleSeatsRoom1 = [10, 5, 6, 8, 0]
availibleSeatsRoom2 = [10, 5, 6, 8, 0]
availibleSeatsRoom3 = [10, 5, 6, 8, 0]
availibleSeatsRoom4 = [10, 5, 6, 8, 0]
availibleSeatsRoom5 = [10, 5, 6, 8, 0]

# Functions -
def invalidInput():
    print('\033[31m\nVocê inseriu algo inválido.\033[0m\nTente novamente!')
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

def seeAvailibleSeats():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[32mVocê escolheu ver as as salas disponíveis!\033[0m\n\nNo momento as salas disponíveis são:\033[35m')
    for room in availibleRooms:
        print(room, end=' | ')
    print('\033[0m')
    chooseRoom()

def chooseRoom():
    while True:
        chosenRoom = input(
            '\nVocê deseja comprar assentos em que sala \033[31m(digite Q para sair)\033[0m? ').strip().lower()
        if chosenRoom == '':
            invalidInput()
            continue
        elif chosenRoom[0] == 'q':
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif chosenRoom in availibleRooms:
            buySeats(chosenRoom)
            break
        else:
            invalidInput()
            continue

def buySeats(room):
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    match(room):
        case "1": seats = availibleSeatsRoom1
        case "2": seats = availibleSeatsRoom2
        case "3": seats = availibleSeatsRoom3
        case "4": seats = availibleSeatsRoom4
        case "5": seats = availibleSeatsRoom5
        case _: seats = 'Erro'
    print(
        f'\nVocê escolheu ver assentos na sala \033[35m[{room}]\033[0m.\n\nOs seguintes assentos estão disponíveis:\033[32m')
    for seat in seats:
        print(seat, end=' | ')
    chosenSeat(seats)
    if not seats:
        validateRoom(room)
    else:
        print('Assentos ainda disponíveis:\033[32m')
        for seat in seats:
            print(seat, end=' | ')
        print('\n\n\033[0m')
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

def validateRoom(room):
    availibleRooms.remove(room)
    print(availibleRooms)

def chosenSeat(seats):
    buySeat = input(
        '\n\n\033[0mQual assento você deseja comprar (para comprar mais de um separe os assentos desejados com ", ")? ')
    if ', ' in buySeat:
        boughtSeats = buySeat.split(', ')
        for boughtSeat in boughtSeats:
            validatingSeats(boughtSeat, seats)
    else:
        validatingSeats(buySeat, seats)

def validatingSeats(seat, seats):
    if seat == '' or not seat[0].capitalize().isdigit():
        invalidInput()
    elif int(seat) in seats:
        while True:
            confirmPurchase = input(
                f'Deseja comprar o asssento - \033[35m{seat}\033[0m? ').strip().lower()
            if confirmPurchase == '':
                continue
            elif confirmPurchase[0] == 's' or confirmPurchase[0] == 'y':
                seats.remove(int(seat))
                print(f'Você comprou o assento \033[32m{seat}\033[0m!\n')
                break
    else:
        invalidInput()

def showCredits():
    print('\n\033[34mObrigado por querer me conhecer\033[0m 😁✌️\nEste programa foi desenvolvido por \033[35m@joas005\033[0m no github, entre lá para conheça um pouco mais sobre mim e meus projetos!')
    time.sleep(1.5)
    input('\nEnter continua...')
    os.system('cls' if os.name == 'nt' else 'clear')

def exitProgram():
    print('\n\033[32mObrigado por escolher o \033[35mcinemarko!\033[0m\nVolte sempre que quiser a melhor experiência possível na sua seção de cinema 😁')
    time.sleep(2)
    exit()

# Main -
print('\033[35m', 10*'-' + '🍿 CINEMARKO🍿 ' + 10*'-' + '\n', '\033[0m')

print('\033[32mBem-vindo ao CINEMARKO\033[0m, aqui você pode comprar do conforto da sua casa ingressos para os melhores e mais novos filmes!\n')

while True:
    menu = input(
        'O que você deseja fazer?\n\033[32m[1] Ver salas com assentos disponíveis.\n\033[34m[2] Créditos.\n\033[31m[3] Sair.\n\033[0m> ')
    match(menu):
        case '1':
            seeAvailibleSeats()
            continue
        case '2':
            showCredits()
            continue
        case '3':
            exitProgram()
        case _:
            invalidInput()
            continue