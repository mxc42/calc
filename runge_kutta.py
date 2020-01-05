def k1(xi, yi):
    return f(xi, yi)

def k2(xi, yi, h):
    return f(xi+h/2, yi + h/2*k1(xi, yi))

def k3(xi, yi, h):
    return f(xi + h/2, yi + h/2*k2(xi, yi, h))

def k4(xi, yi, h):
    return f(xi + h, yi + h*k3(xi, yi, h))

def m(x0, y0, h, max_x):
    n = 0
    x = x0
    y = y0
    while(x <= max_x):
        print('x_{:d} = {:f}, y_{:d} = {:f}'.format(n,x,n,y))
        t = x
        x = x + h
        y = y + h/6*(k1(t, y) + 2*k2(t, y, h) + 2*k3(t, y, h) + k4(t, y, h))
        n += 1

