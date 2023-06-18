from collections import Counter
import re
def top_3_words(text):
    reg = re.compile("[^a-zA-Z ']")
    text = reg.sub(' ', text).lower().split()
    
    while "  " in text:
        text = text.replace("  ", " ");
        
    text = [i[0] for i in Counter(text).most_common(len(set(text)))]
    
    for i in range(len(text)):
        if re.search('[a-z]', text[i]) is None:
            text[i] = ''
            
    while '' in text: text.remove('')
    return text[:3]