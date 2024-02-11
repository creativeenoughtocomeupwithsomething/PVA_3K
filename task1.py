import math


def pipes(A, B):
    pipe = abs(A[0]- B[0]) + abs(A[1] - B[1]) + abs(A[2] + B[2])
    print(pipe)

def ropes(A, B):
    X_lenght = abs(A[0] - B[0])
    Y_lenght = abs(A[1] - B[1])
    Z_lenght = abs(A[2] - B[2])
    scale = X_lenght + Y_lenght

    Zx_lenght = (Z_lenght / scale) * X_lenght
    ZY_lenght = (Z_lenght / scale) * Y_lenght
    length = math.sqrt((X_lenght * X_lenght) + (Zx_lenght * Zx_lenght)) + math.sqrt((Y_lenght * Y_lenght) + (Zy_lenght * Zy_lenght)) 
    print(length)

try:
    room = input("Room size: ")
    A = [int(x) for x in input("point #1 cordinates: ").split()]
    B = [int(x) for x in input("Point #2 cordinates: ").split()]
    print(A)
    print(B)
    if len(B) != len(A) != 3:
        raise

    elif A[0] != 0 and A[0] != room and  A[1] != 0 and A[1] != room and  A[2] != 0 and A[2] != room:
        raise

    elif B[0] != 0 and B[0] != room and  B[1] != 0 and B[1] != room and  B[2] != 0 and B[2] != room:
        raise
    else:
        print("Room size: \n" + room)
        print("Point #1: \n" + A)
        print("Point #2: \n" + B)
        print("Length #1: \n" + pipes(A, B))
        print("Length #2: \n" + ropes(A, B))
    
    

except:
    print("Error on input")





    ## A[0] != 0 and A[0] != room and  A[1] != 0 and A[1] != room and  A[2] != 0 and A[2] != room: