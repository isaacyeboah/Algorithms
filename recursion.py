from stack import Stack


def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])


def toStr(n, base):
    rStack = Stack()
    convertString = '0123456789ABCDEF'
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])

        n = n // base

    res = ''
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res


if __name__ == '__main__':
    # print(listsum([1, 3, 5, 7, 9]))
    print(toStr(1453, 16))
