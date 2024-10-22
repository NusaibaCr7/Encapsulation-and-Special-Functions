class Word:
    
    def __init__(self,w):
        self.w = w
        
    def revStr(self):
        return self.w[::-1]
        
word = input("Enter a word: ")

o1 = Word(word)
print(o1.revStr())