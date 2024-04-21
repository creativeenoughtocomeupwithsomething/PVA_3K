def check(val):
    if len(val) < 2 or len(val) > 2000:
        print("Wrong input size")
    else:
        for x in val:
            if type(x) == num:
                return val
            
def lookup(val):
    addup = []
    for i in range(len(val)):
        for j in range(i + 2, len(val) + 1):
            addup.append(sum(inp[i:j]))
    sumset = tuple(set(addup))
    multiples = [[num]*addup.count(num) for addup in sumset if addup.count(num) > 1]
    res = 0
    for i in multiples:
        res += len(i)* (len(i) - 1) // 2
    return res

print(lookup(check(input("Input interval: "))))