import random
count=5
n=random.randint(1,100) 
while (count>0):
   x=int(input(" please enter the number:")) 
   if (x < n):
      print("Too low")
   elif x > n :
     print("Too high") 
   else:
    print("you won") 
    break;       
    count=-1 
    print("you lost")
