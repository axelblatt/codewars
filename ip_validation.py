def is_valid_IP(strng):
    b = strng.replace('.','');
    
    if b.isdigit() and strng.count('.') == 3:
        n = strng.split('.');
        
        for i in n:
            
            if len(i) > 1:
                if i[0] == '0':
                    return False;
                    break;
                for i in n:
                    if int(i) > 255:
                        return False;
                        break;
            
        l = 0;
            
        for i in n:
            l = l + int(i);
            
        if l <= 1020:
            return True;
            
        else:
            return False;
        
    else:
        return False;