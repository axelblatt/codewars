def solution(number):
    summary = 0;
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            summary += i;
    
    return summary;