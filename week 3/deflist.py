def printelements(elements): 
    for i in elements: 
       print(i,end=" ")
elements=[]
limit=int(input("enter the limit")) 
for i in  range(limit):
       ele=int(input("enter"))
       elements.append(ele)
printelements(elements)
