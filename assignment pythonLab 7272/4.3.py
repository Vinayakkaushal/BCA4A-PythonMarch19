#WAP to show the working of break and continue statement
for i in range(1,101):
    if i%2==0:
        if i==50:
            break
        print(i)
    else:
        if i==50:
            continue
        print(i)