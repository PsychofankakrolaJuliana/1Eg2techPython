import msvcrt
import os

def ConsoleClear():
    os.system('cls' if os.name =="nt" else 'clear')

def ConsoleReadKey():
    print("Nacisnij dowolny klawisz...")
    key = msvcrt.getch()

def CzyAnagram(napis):
    w=""
    for i in range(len(napis)-1,-1,-1):
        w+=napis[i]
    if w==napis:
        return True
    else:
        return False
    
def OdwroconyWyraz(napis):
    w=""
    for i in range(len(napis)-1,-1,-1):
        w+=napis[i]
    return w

def Menu():
    choice = 0
    while(True):
        ConsoleClear()
        print("\nMenu:")
        print("1. Sprawdź czy wyraz jest anagramem.")
        print("2. Wyswiel odwrócony wyraz.")
        print("3. Zamknij program")
        print("Podaj wybor: ")
        choice = int(input())
        while(choice>3 or choice<1):
            print("Podano nieprawidlowy numer.")
            choice = input()
        if(choice == 1):
            print("\nPodaj napis: ")
            napis=input()
            if(CzyAnagram(napis)):
                print("\nPodany wyraz jest anagramem")
            else:
                print("Podany wyraz nie jest anagramem")
            ConsoleReadKey()
            ConsoleClear()
            Menu()
            break
        elif(choice == 2):
            print("\nPodaj napis: ")
            napis=input()
            print("\n",napis, " -> ",OdwroconyWyraz(napis))
            ConsoleReadKey()
            ConsoleClear()
            Menu()
            break
        elif(choice == 3):
            ConsoleClear()
            print("Koniec programu.")
            ConsoleReadKey()
            break

Menu()
