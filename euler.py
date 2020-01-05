def m(x_0, y_0, h, max_x):
    n = 0
    x = x_0
    y = y_0
    print('x_{:d} = {:f}, y_{:d} = {:f}'.format(n,x,n,y))
    while(x < max_x):
        t = x
        x = x + h
        y = y + h*f(t,y)
        n += 1
        print('x_{:d} = {:f}, y_{:d} = {:f}'.format(n,x,n,y))
    return y
