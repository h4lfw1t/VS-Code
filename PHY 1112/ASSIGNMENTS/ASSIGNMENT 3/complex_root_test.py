def root(a,b,c):
    # Calculate the discriminant
    z = b**2 - 4*a*c
    r = abs(z)

    print(z)
    print(r)
    print(r**0.5)
    print(z+r)
    print(abs(z+r))
    print(2*r)
    print(r**0.5*((z+r)/abs(z+r)))
    
    root1 = (-b + r**0.5*((z+r)/abs(z+r))) / (2*a)
    root2 = (-b - r**0.5*((z+r)/abs(z+r))) / (2*a)
    
    print(root1)
    print(root2)

root(1,-(-1-1j),1j)