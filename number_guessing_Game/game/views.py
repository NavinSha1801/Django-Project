from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
def guess_game(request):
    print("Lets Play number guessing Game")
    random_no = random.randint(0,100)
    Guessings = 1
    total_lst = []
    print('''\n \'\'\'If you want some help then type hint/h so that you can get range of number 
    and if you want to quit game type exit/e to quit game\'\'\' \n''')
    choosen_number = input("Enter the your first choice: ")
    while True:
        if choosen_number.isdigit():
            choosen_number = int(choosen_number)
            break
        else:
            print("Kindly Enter Number only")
            choosen_number = input("Enter the number again: ")
    while True: 
        if choosen_number>(random_no+10):
            print("Hmm too high low your choice bit")
            choosen_number = input("Enter the number: ")
            while True:
                if choosen_number.isdigit():
                    choosen_number = int(choosen_number)
                    break
                elif choosen_number == 'h' or choosen_number =='H' or choosen_number == 'HINT' or choosen_number == 'Hint' or choosen_number == 'hint':
                    print(f"Hint:- The number lies in range of {random_no-11} and {random_no+12}")
                    choosen_number = input("Enter the number: ")
                elif choosen_number == 'e' or choosen_number =='E' or choosen_number == 'EXIT' or choosen_number == 'Exit' or choosen_number == 'exit':
                    print("Thank you for playing with us")
                    exit()
                else:
                    print("Kindly Enter Number only")
                    choosen_number = input("Enter the number: ")
            Guessings += 1
        elif choosen_number<(random_no+10) and choosen_number>random_no:
            print("Hmm Little high low your choice bit")
            choosen_number = input("Enter the number: ")
            while True:
                if choosen_number.isdigit():
                    choosen_number = int(choosen_number)
                    break
                elif choosen_number == 'h' or choosen_number =='H' or choosen_number == 'HINT' or choosen_number == 'Hint' or choosen_number == 'hint':
                    print(f"Hint:- The number lies in range of {random_no-11} and {random_no+12}")
                    choosen_number = input("Enter the number: ")
                elif choosen_number == 'e' or choosen_number =='E' or choosen_number == 'EXIT' or choosen_number == 'Exit' or choosen_number == 'exit':
                    print("Thank you for playing with us")
                    exit()
                else:
                    print("Kindly Enter Number only")
                    choosen_number = input("Enter the number: ")
            Guessings += 1
        elif choosen_number<(random_no-10):
            print("Hmm too low high your choice bit")
            choosen_number = input("Enter the number: ")
            while True:
                if choosen_number.isdigit():
                    choosen_number = int(choosen_number)
                    break
                elif choosen_number == 'h' or choosen_number =='H' or choosen_number == 'HINT' or choosen_number == 'Hint' or choosen_number == 'hint':
                    print(f"Hint:- The number lies in range of {random_no-11} and {random_no+12}")
                    choosen_number = input("Enter the number: ")
                elif choosen_number == 'e' or choosen_number =='E' or choosen_number == 'EXIT' or choosen_number == 'Exit' or choosen_number == 'exit':
                    print("Thank you for playing with us")
                    exit()
                else:
                    print("Kindly Enter Number only")
                    choosen_number = input("Enter the number: ")
            Guessings += 1
        elif choosen_number>(random_no-10) and choosen_number<random_no:
            print("Hmm little low high your choice bit")
            choosen_number = input("Enter the number: ")
            while True:
                if choosen_number.isdigit():
                    choosen_number = int(choosen_number)
                    break
                elif choosen_number.startswith("h") or choosen_number.startswith("H"):
                    print(f"Hint:- The number lies in range of {random_no-11} and {random_no+12}")
                    choosen_number = input("Enter the number: ")
                elif choosen_number == 'e' or choosen_number =='E' or choosen_number == 'EXIT' or choosen_number == 'Exit' or choosen_number == 'exit':
                    print("Thank you for playing with us")
                    exit()
                else:
                    print("Kindly Enter Number only")
                    choosen_number = input("Enter the number: ")
            Guessings += 1
        else:
            print(f"You got that number and your total number of guess is {Guessings}")
            total_lst.append(Guessings)
            break
    if Guessings>=15:
        print(f"Your average Guessing Rate is Low")
    elif Guessings<15 and Guessings>=10:
        print("Your Average Guessing Rate is moderate")
    elif Guessings<10 and Guessings>=5:
        print("your Average Guessing Rate is medium")
    else:
        print("Your Average Guessing Rate is awsome")

def index(request):
    return HttpResponse("Hello World!")