def Fizzbuzz():

    wsz = ""
    for x in range(1,101):
        y = ""
        z = ""
        c = ""
        if x%15==0:
            y = "fizzbuzz"
            wsz += str(y) + "\n"
        elif x%3==0:
            z = "fizz"
            wsz += str(z) + "\n"
        elif x%5==0:
            c = "buzz"
            wsz += str(c) + "\n"
        else:
            wsz += str(x) + "\n"
    return wsz

print(Fizzbuzz())
