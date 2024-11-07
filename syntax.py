
# In Python, a character is a string of length 1.

def inWord( ch : str ) -> bool :
   if ch == "'" or ch == '`' :
      return True 

   if ch == '-' :
      return True

   if '0' <= ch and ch <= '9' : 
      return True

   return ch. isalpha( ) 

def isNewLine( ch : str ) -> bool :
   return ch == '\n'


