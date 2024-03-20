u = []
i = 0

while i < 100:
    s = input("Click 'q' to quit - Enter the number: ")
    if s != 'q':
        u.append(s)
    else:
        print("You are out")
        break
    i += 1

print(u)
