name = str(input("Enter your string  "))
for i in range(0, int(len(name) / 2)):
    if name[i] != name[int(len(name))-i-1]:
        print("String is not palindrum ")
        break
    else:
        print("String is palindrum")


