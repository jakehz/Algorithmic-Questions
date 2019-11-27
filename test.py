def doThing():
    for i in range(0,9):
        for j in range(0,9):
            print("i: " + str(i) + " -> " + str(3*(i%3) + j//3) + " j: " + str(j) + " -> " + str(j%3 + 3*(i//3)))