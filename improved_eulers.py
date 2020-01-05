def m1(xi, yi):
    return f(xi, yi)

def m2(xi, yi, h):
    return f(xi+h, yi + h*m1(xi, yi))

def i_euler(x0, y0, h, max_x):
    n = 0
    x = x0
    y = y0
    print('x_{:d} = {:f}, y_{:d} = {:f}'.format(n,x,n,y))
    while(x < max_x):
        t = x
        x = x + h
        y = y + h*(m1(t, y) + m2(t, y, h))/2
        n += 1
        print('x_{:d} = {:f}, y_{:d} = {:f}'.format(n,x,n,y))
    return y
