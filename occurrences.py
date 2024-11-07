
from fileposition import FilePosition
from typing import List, Dict, Set, Optional 

class Occurrences : 
   occs : Dict[ str, Dict[ str, Set[ FilePosition ]]] 

   def __init__( self ) :
      self. occs = dict( ) 


   def add( self, word : str, filename : str, pos : FilePosition ) -> None :

 
   # Should return the number of distinct words:
 
   def distinctWords( self ) -> int : 

    
   # Should return the total number of words occurrences: 
 
   def totalOccurrences( self, word : Optional[str] = None, 
                               fname : Optional[str] = None ) -> int : 


   # This is for debugging, so it doesn't need to be pretty: 

   def __repr__( self ) -> str : 
      return str( self. occs )

 
   # Here the occurrences must be sorted and shown in a nice way: 

   def __str__( self ) -> str : 
 
