def series(n):
    x,y=2,3
    while (x<n):
        print(x)
        x,y=y,x+y
        series(30)