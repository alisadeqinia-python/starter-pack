#Draw Stars in ROWS
def star_row(count):
    count=int(input("How many stars in lines you want?"))
    space=count-1
    for i in range(count):
        for j in range(space):
            print(end=" ")
        space-=1
        for l in range(i+1):
            print("*",end=" ")
        print("\r")
