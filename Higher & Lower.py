import random
import sys
import string

#This function would display the scoreboard on the screen and top 10 players score listing
def high_scores(name,scores):
        scores_sorted_keys = sorted(scores, key=scores.get, reverse=True)
        x=0
        for key in scores_sorted_keys:
                if name==key:
                        print("%s: %s <- Your Score" % (key,scores.get(key)))
                else:
                        print("%s: %s" % (key,scores.get(key)))
                x+=1
                if x == 10:
                        break
        return

def seperator():
        print("\n"*10)
        
def decorator():
        print("*"*20)

def homepage(scores,name="System",difficulty=1):
        seperator()
        print("\t"*5+"*GAMING HUB*")
        print("\nSelect Options:\n1. Play Higher & Lower Game\n2. Scoreboard\n3. Options\n4. Exit\n")
        option=int(input("Your Choice:\t"))
        if option==1:
                gameplay(name,difficulty,scores)
        elif option==2:
                high_scores(name,scores)
        elif option==3:
                difficulty=show_option()
                gameplay(name,difficulty,scores)
        elif option==4:
                sys.exit()
        else:
                print("Invalid Entry!")
        homepage(scores,name,difficulty)

def show_option():
        seperator()
        print("\t"*5+"*Options*")
        print("\nSelect Difficulty Level:\n1. Easy Level (5 Chance: Range (1 to 100)\n2. Hard Level (20 Chance: Range (1 to 1000)\n3. Pro Level (1 Chance: Range (1 to 10))\n4. Back to Home")
        difficulty=int(input("Choice:\t"))
        if difficulty in (1,2,3):
                return difficulty
        else:
                print("Invalid Selection!")
                show_option()
        
def title(points):
        seperator()
        print("**** Higher & Lower Game ****\nPoints: %s "  % points)
        guess=int(input("Enter your guess:\t"))
        return guess
   
def gameplay(name, difficulty,scores):
        (response,win_flag)="Y","No"

        while response=="Y" or response=="y":
                points=0
                if difficulty==1:
                        (attempt,limit,point_range)=5,100,10
                elif difficulty==2:
                        (attempt,limit,point_range)=20,1000,100
                else:
                        (attempt,limit,point_range)=1,10,0
                        
                spare_attempt=attempt
                rand=random.choice(range(1,limit))
                for x in range(attempt):
                        spare_attempt-=1
                        guess=title(points)
        
                        if guess>limit or guess<1:
                                print("Enter a Valid Number! Attempt Lost!")
                                continue
                        elif guess==rand:
                                points+=100     
                                print("You win!!")
                                win_flag="Yes"
                                break
                        else:
                                if abs(guess-rand)<point_range:
                                        points+=20
                                if guess > rand:
                                        print("Your guesss %s is higher." % guess)
                                elif guess < rand:
                                        print("Your guesss %s is lower." % guess)
                     
                points+=spare_attempt*100
                print("Points Earned: %s" % points)

                found_key="No"
                for key in scores.keys():
                        if name==key:
                                found_key="Yes"
                                if int(scores.get(name)) < points:
                                        print("New High Score for %s" % name)
                                        override=input("Enter a new name (Y) or Override above mentioned name's score? (any other key):\t")
                                        if override == 'Y' or override == 'y':
                                                name=input("Enter New Name for storing highest score:\t")
                                        scores[name]=points
                if found_key=="No":
                        scores[name]=points
                write_scores_to_file(scores)
                if spare_attempt == 0 and win_flag=="No":
                        print("You Loose the Game! \nTry Again! %s was the generated number" % rand)
                response=input("Do you want to play again? Y or N\n")
        return

def read_scores_from_file():
        scores={}
        with open("output.txt") as f:
                for line in f:
                        (key, val) = line.split("\t")
                        scores[key] = int(val)
        f.close()
        return scores

def write_scores_to_file(scores):
        output = open('output.txt', 'w+')
        for key, value in scores.items():
                output.write(str(key))
                output.write(str("\t"+str(value)+"\n"))
        output.close()
                        
def init():
        scores=dict(read_scores_from_file())
        name_1=input("Enter your Name:\t")
        if name_1 == None:
                name="System"
        else:
                name=string.capwords(name_1)
        print("Welcome %s, set difficulty level by selecting Options or Play at Easy Level!"% name)
        homepage(scores,name)

init()
