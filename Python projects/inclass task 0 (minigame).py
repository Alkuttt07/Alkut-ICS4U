import random
Paper=1
Rock=2
Scissors=3
opponent= (Paper,Rock,Scissors)

yourchoice=(0)
while 1>0:
    randomopponent=random.choice(opponent)
    yourchoice=input("""Welcome to Paper,Rock and scissors game, please select the order of your choice
  1.Paper
  2.Rock
  3.Scissors
 """)
    try: 
        yourchoice=int(yourchoice)
        if (yourchoice - randomopponent == 0) and (1<=yourchoice<=3):
            a=input("""You have the same choice with the opponent, press 'r' to restart or press anything else to stop
 """)
            if a==("r"):
                continue
            else:
                break
        elif ((yourchoice - randomopponent == 1) or (yourchoice - randomopponent == -2)) and 1<=yourchoice<=3:
            a=input("""You failed the game, press 'r' to restart or press anything else to stop
 """)
            if a==("r"):
                continue
            else:
                break
        elif ((yourchoice - randomopponent == -1)or (yourchoice - randomopponent == 2)) and 1<=yourchoice<=3:
            a=input("""You won the game, press 'r' to restart or press anything else to stop
 """)
            if a==("r"):
                continue
            else:
                break
        else:
            a=input("""Your choice is not representing the options given. 
Press 'r' to restart or press anything else to stop
 """)
            if a==("r"):
                continue
            else:
                break
    except:
        a=input("""Your answer is invalid. 
Press 'r' to restart or press anything else to stop
 """)
        if a==("r"):
            continue
        else:
            break