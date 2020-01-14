def fb(N):
    res = ""
    if N % 3 == 0:
        res += "Fizz"
    if N % 5 == 0:
        res += "Buzz"
    if len(res) == 0:
        res = str(N)
    return res
