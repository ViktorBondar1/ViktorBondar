a=int(input("Proszę podać a "))
b=int(input("Proszę podać b "))
if(a>b):
    c=b
    d=a
else:
    c=a
    d=b
while(c<=d):
    if c%2:
        c=1

        continue


    print(c, end=" ")
    c+=1