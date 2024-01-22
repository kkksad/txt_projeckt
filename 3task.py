file=open('travels.txt', 'r')
Dict1=dict()
summa=0
dist=0
dict2=dict()
for i in file:
    
    if i.split()[2]=="Липки":
        summa+=int(i.split()[6])
    if i.split()[0]=="1" and i.split()[1]=="октября":
        
        dist+=int(i.split()[4])
    key=str(i.split()[0]+i.split()[1])
    if key in list(Dict1.keys()):
        Dict1[key]+=int(i.split()[6])
    else:
        Dict1[key]=int(i.split()[6])
list1=[]
for i in Dict1:
    list1.append(int(Dict1[i]))
maxim=max(list1)
for i in Dict1:
    if Dict1[i]==maxim:
        print(f"{i} : {Dict1[i]}")

print(summa)
print(dist)
