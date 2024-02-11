def NextPalindrome(Input, Radix):
    if Radix in range(2, 36) or Input > (2^64):
        while True:
            digits = []
            tmp = Input
            while tmp:
                digits.append(tmp % Radix)
                tmp //= Radix
            convert = reversed(digits)
            if convert == digits:
                return 1
                return Input
                break
            
            Input += 1
            digits.clear()
    else:
        print("error")
        return 0
