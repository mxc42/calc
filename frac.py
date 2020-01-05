def main(x):
    max_test = 2000
    is_negative = False
    if (x < 0):
        is_negative = True
    x = abs(x)
    x = round(x, 16)
    test = int(x - 1)
    for i in range (test, max_test):
        for j in range (1, max_test):
            if (x == i/j):
                if is_negative:
                    print('-', end='')
                print(str(i)+'/' + str(j))
                return
    print("no solution found with max_test = " + str(max_test))
