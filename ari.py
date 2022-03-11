def ari_emptychar(s):
     if len(s)==0:
          return 0
def ari_alphanumeric(s):
     if not s.isalnum():
       return False
def ari_numcharectors(s):
     acc=0
     for i in s:
          acc+=1
     return acc
def ari_emptyword(s):
     if " " not in s:
          return None
def ari_numword(s):
     acc=0
     for i in s:
          if i ==' ':
               acc+=1
     return acc
def ari_emptysentence(s):
     if "." or "!" or"?" not in s:
          return None         
def ari_sentences(s):
     acc=0
     for i in s:
          if i == '!' or i == '?' or i == '.':
               acc+=1
     return acc