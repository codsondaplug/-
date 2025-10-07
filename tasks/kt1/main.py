import random

n=int()
print("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК!?")
answer = input()
while n<3:
    first_number = random.randint(3, 5)
    second_number = random.randint(0, 9)
    if answer.isupper():
        print("НЕТ,НИ РАЗУ С 19"+str(first_number)+str(second_number)+ " ГОДА!")
    else:
        print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")
    answer=input()
    if answer=="ПОКА!":
        n+=1
        if n==3:
            print("ДО СВИДАНИЯ, МИЛЫЙ!")
