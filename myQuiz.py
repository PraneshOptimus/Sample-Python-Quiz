import time as t

name = str(input("Whats Your Name ? "))
print("\nWelcome To The Quiz",name,"!!")

score = 0
def SM():
    global score
    score += 1
    print("The Current Score is :",score)

print("\n1) who is the president of india? ")
t.sleep(0.5)
print("a) Stalin")
print("b) vijay")
print("c) Narendra Modi")
print("d) Draubadi murmu\n")

answer = str(input("Enter Your Answer: "))
if answer == "c":
    print("You are correct , Proceeding To Next Question")
    SM()
else:
    print("Answer is Wrong")
t.sleep(2)
print("\n2) who is vijay? ")
t.sleep(0.5)
print("a) Actor")
print("b) Sportsperson")
print("c) Driver")
print("d) Painter\n")
answer = str(input("Enter Your Answer: "))
if answer == "a":
    print("You are correct , Proceeding To Next Question")
    SM()
else:
    print("Answer is Wrong")
t.sleep(2)

print("\n3) who is wife of Virat Kohli? ")
t.sleep(0.5)
print("a) Keerthi shetty")
print("b) Anuskha Sharma")
print("c) Samantha")
print("d) Hansika\n")

answer = str(input("Enter Your Answer: "))
    
if answer == "b":
    print("You are correct , Proceeding To Next Question")
    SM()
else:
    print("Answer is Wrong")
if score == 1:
    print("Your Score is 1/5")
elif score == 2:
    print("Your Score is 2/5")
elif score == 3:
    print("Your Score is 3/5")
elif score == 4:
    print("Your Score is 4/5")
elif score == 5:
    print("Your Score is 5/5")
else:
    print("You Piece Of Shit")

