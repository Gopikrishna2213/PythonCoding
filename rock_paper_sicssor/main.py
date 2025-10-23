import random
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
sicssor=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
k=[rock,paper,sicssor]
n=int(input('hoose anything you want?\n0.rock\n1.paper\n2.sicssor')) 
if n>=3 or n<0:
    print('you entered invalid number\nyou lose!')
else :
    print("your's")
    print(k[n])
r=random.randint(0,2)
print("computer's")
print(k[r])
if n==r:
    print("it's draw")
elif n==0 and r==2:
    print("YOU WIN!")
elif r==0 and n==2:
    print("YOU LOSE!")
elif n>r:
    print("YOU WIN!")
elif r>n:
    print("YOU LOSE!")
