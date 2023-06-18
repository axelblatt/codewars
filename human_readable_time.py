def make_readable(seconds):
    hours = seconds // 3600;
    seconds = seconds - hours * 3600;
    
    minutes = seconds // 60;
    seconds = seconds - minutes * 60;
    
    if hours < 10: hours = '0' + str(hours); 
    if minutes < 10: minutes = '0' + str(minutes); 
    if seconds < 10: seconds = '0' + str(seconds); 
    
    
    return '{}:{}:{}'.format(hours, minutes, seconds);