

def do_it(a,b,*args,d=4,**kwargs):
    print(a, b, args, d, kwargs)


do_it(1,2,4,5,e=2,f=4, d=99)