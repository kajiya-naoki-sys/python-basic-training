#print(1 / 0)
try:
    print(1 / 0)
except ZeroDivisionError:
    print("Error")