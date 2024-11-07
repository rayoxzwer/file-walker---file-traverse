

class FilePosition : 
   line : int
   column : int

   def __init__( self ) :
      self. line = 1
      self. column = 1

   def advance( self, i : int ) :
      self. column += i

   def nextLine( self ) :
      self. line += 1
      self. column = 1

   def __repr__( self ) -> str : 
      return "( {}, {} )". format( self. line, self. column )

   def __str__( self ) -> str :
      return "line " + str( self. line ) + ", column " + str( self. column )



   def __hash__( self ) -> int :

   def __eq__( self, other ) -> bool :
   
   def __lt__( self, other ) -> bool :

