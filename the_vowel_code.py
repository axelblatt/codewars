def encode(st):
    a = ['a', 'e', 'i', 'o', 'u'];
    for i in range(len(a)):
        st = st.replace(a[i], str(i + 1));
    return st;
    
def decode(st):
    a = ['a', 'e', 'i', 'o', 'u'];
    for i in range(len(a)):
        st = st.replace(str(i + 1), a[i]);
    return st;