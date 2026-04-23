x = 6

def examples():
    
    globx = x 
    
    print(globx)

    globx += 5
    print(globx)

    return globx
    

examples()

x = examples()    # captures return value in x, prints 6 and 11 

print(x)          # prints captured value