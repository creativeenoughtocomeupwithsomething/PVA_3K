try:
    from operator import itemgetter
    A = [float(x) for x in input("Point A cordinates: ").split()]
    B = [float(x) for x in input("Point B cordinates: ").split()]
    C = [float(x) for x in input("Point C cordinates: ").split()]

    if len(A) != len(B) != len(C) != 2:
        print("flag1")
        raise
    elif A == B or A == C or B == C:
        print("identical")
    elif (A[1] - B[1]) * (A[0] - C[0]) == (A[1] - C[1]) * (A[0] - B[0]):
        D = [A, B, C]
        if A[0] == B[0] == C[0]:
            sorted_X = sorted(D, key=itemgetter(1))
        else:
            sorted_X = sorted(D, key=itemgetter(0))
        print("on a line")
        print(sorted_X[1])
        print(A)
        print(B)
        print(C)
        if sorted_X[1] == A:
            print("A is in the middle")
        elif sorted_X[1] == B:
            print("B is in the middle")
        elif sorted_D[1] == C:
            print("C is in the middle")
    else:
        print("not on a line")
except:
    print("error on input")