def maior_numero(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(maior_numero(10, 20, 15))  
print(maior_numero(5, 3, 8))  
print(maior_numero(7, 7, 7))   
