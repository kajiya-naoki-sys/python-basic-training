try:
    with open("/test.txt") as f:
        print(type(f))
except FileNotFoundError:
    print("FileNotFoundError")