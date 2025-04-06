import random

while True:
    player=["rock","paper","scissor"]
    #computer=["r","p","s"]
    print()
    print("\t\t==============================")
    print()
    print("\t\t",player)
    print()
    p=input("\t\tENTER YUOR CHOICE : ")
    c=random.choice(player)
    if p in player:
        if p==c:
            print()
            print("\t\t==============================")
            print()
            print("\t\tCPU : ",c,end="    ")
            print("PLAYER : ",p)
            print() 
            print("\t\t\tTIE")
        elif c=="rock" and p=="paper":
            print()
            print("\t\t==============================")
            print()
            print("\t\tCPU : rock",end="    ")
            print("PLAYER : paper")
            print()
            print("\t\t\tPLAYER WIN")
        elif c=="rock" and p=="scissor":
            print()
            print("\t\t==============================")
            print()
            print("\t\tCPU : rock",end="    ")
            print("PLAYER : scissor")
            print()
            print("\t\t\tCPU WIN")
        elif c=="paper" and p=="rock":
            print()
            print("\t\t==============================")
            print()
            print("\t\tCPU : paper",end="    ")
            print("PLAYER : rock")
            print()
            print("\t\t\tCPU WIN")
        elif c=="paper" and p=="scissor":
            print()
            print("\t\t==============================")
            print()
            print("\t\tCPU : paper",end="    ")
            print("PLAYER : scissor")
            print()
            print("\t\t\tPLAYER WIN")
        elif c=="scissor" and p=="rock":
            print()
            print("\t\t==============================")
            print()
            print("\t\tCPU : scissor",end="    ")
            print("PLAYER : rock")
            print()
            print("\t\t\tPLAYER WIN")
        elif c=="scissor" and p=="paper":
            print()
            print("\t\t==============================")
            print()
            print("\t\tCPU : scissor",end="    ")
            print("PLAYER : paper")
            print()
            print("\t\t\tCPU WIN")
    else:
        print()
        print("\t\tCHOOSE SOME ONE IN GIVEN LIST")