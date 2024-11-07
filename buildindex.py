
from fileposition import FilePosition
from occurrences import Occurrences
from filewalker import FileWalker

import codecs

def index( topdir : str ) -> None :
   print( "" ) 
   print( "the top directory is " + topdir )
   print( "" )

   fw = FileWalker( topdir )

   occ = Occurrences( )

   try :
      for fname, word, position in fw. recDirIterator( ) :
         occ. add( word, fname, position )

   except Exception as ex:
      print( "there was an exception: " + str( ex ))

   print( occ ) 

   if True: 
      file = open( "output_for_" + topdir + ".txt", "w", encoding = "utf8" )
      file. write( str( occ ) + "\n" )
      file. write( "number of distinct words  " + str( occ. distinctWords( )) + "\n" )
      file. write( "number of occurrences     " + str( occ. totalOccurrences( )) + "\n" )
      file. write( "\n" )
      file. close( ) 

index( "dir1" )

