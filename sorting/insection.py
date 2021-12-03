def insertionsort(alist):
    for i in range(1, len(alist)):
        curval = alist[i]
        curpos = i
        while curpos > 0 and alist[curpos - 1] > curval:
            alist[curpos] = alist[curpos - 1]
            curpos = curpos - 1
        alist[curpos] = curval


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertionsort(alist)
    print(alist)