def applytoeach(L,x):
    for f in L:
        print(f(x))
        
applytoeach([abs, float, int], -5)
