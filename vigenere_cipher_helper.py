class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key;
        self.alphabet = alphabet;
        
    def encode(self, text):
        k1 = self.key;
        while len(k1) < len(text):
            k1 += k1;
        k1 = k1[:len(text)];
        
        c = '';
        for i in range(len(text)):
            if text[i] in self.alphabet:
                n = self.alphabet.index(text[i]) + self.alphabet.index(k1[i]);
                while n >= len(self.alphabet):
                    n -= len(self.alphabet);
                c += self.alphabet[n];
            else:
                c += text[i];
        
        return c;
        
    
    def decode(self, text):
        k1 = self.key;
        while len(k1) < len(text):
            k1 += k1;
        k1 = k1[:len(text)];
        
        c = '';
        for i in range(len(text)):
            if text[i] in self.alphabet:
                n = self.alphabet.index(text[i]) - self.alphabet.index(k1[i]);
                while n >= len(self.alphabet):
                    n -= len(self.alphabet);
                c += self.alphabet[n];
            else:
                c += text[i];
        
        return c;