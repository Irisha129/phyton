
a = "STALKER"
m=0
for i in a:
    m += 1
    if m==4 or m==6:
        print (i, end="")
        continue
    print (i, end=".")
print(" ")
