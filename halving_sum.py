def halving_sum(n): 
    
    i = 2;
    s = n;
    
    while n != 1:
        n = n // 2;
        s += n;
        i += 2;
        
    return s;