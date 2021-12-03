from stack import Stack
from deque import Deque


def reverse_string(str):
    s = Stack()
    for ch in str:
        s.push(ch)
    revstr = ''
    while not s.isEmpty():
        revstr += s.pop()
    return revstr


def symbolChecker(symbolString):
    s = Stack()
    balanced = True
    i = 0
    while i < len(symbolString) and balanced:
        symbol = symbolString[i]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        i += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)


def divideBy2(decNumber):
    s = Stack()
    while decNumber > 0:
        remainder = decNumber % 2
        s.push(remainder)
        decNumber = decNumber // 2
    binStr = ""
    while not s.isEmpty():
        binStr += str(s.pop())
    return binStr


def baseConverter(decNumber, base):
    s = Stack()
    digits = "0123456789ABCDEF"
    while decNumber > 0:
        remainder = decNumber % base
        s.push(remainder)
        decNumber = decNumber // base

    convertStr = ""
    while not s.isEmpty():
        convertStr += digits[s.pop()]
    return convertStr


def palindromChecker(aString):
    charDeque = Deque()

    for ch in aString:
        charDeque.addRear(ch)

    stillEqual = True

    while charDeque.size() > 1 and stillEqual:
        first = charDeque.removeFront()
        last = charDeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual


if __name__ == '__main__':
    # print(reverse_string('apple'))
    # print(symbolChecker('{({([][])}())}'))
    # print(divideBy2(42))
    # print(baseConverter(42, 2))
    # print(baseConverter(255, 16))
    # print(baseConverter(26, 26))
    print(palindromChecker("madam"))
