#factorial de un numero con instruccion while
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

print ("%s" % factorial(10))
