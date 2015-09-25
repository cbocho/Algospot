su = input('su : ')
su = int(su)
lst_view = [0 for _ in range(su)]

for n in range(0, su):
    num1 = input("input : ")
    num2 = input("input : ")
    num3 = input("input : ")
    result_lst = ['' for _ in range(su)]

    n1 = num1.split()
    n2 = num2.split()
    n3 =num3.split()

    x1 = int(n1[0])
    x2 = int(n2[0])
    x3 = int(n3[0])
    y1 = int(n1[1])
    y2 = int(n2[1])
    y3 = int(n3[1])

    if x1 == x2:
        x4 = x3
    else:
        if x1 == x3:
            x4 = x2
        else:
            x4 = x1

    if y1 == y2:
        y4 = y3
    else:
        if y1 == y3:
            y4 = y2
        else:
            y4 = y1

    x4 = str(x4)
    y4 = str(y4)

    result = x4+' '+y4
    lst_view.pop(0)
    lst_view.append(result)

print( "\n".join(map(str, lst_view)))
