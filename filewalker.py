
from fileposition import FilePosition
from typing import Tuple, Generator, TextIO 

import os
import syntax
import copy
import codecs


class FileWalker : 
   topdir : str  # Python uses strings for representing file names. 
  
   def __init__( self, topdir ) :
      self. topdir = topdir # No checks here. 


   def recDirIterator( self ) -> Generator[ Tuple[ str, str, FilePosition ], None, None ] : 


   @staticmethod 
   def fileIterator( f : TextIO ) -> Generator[ Tuple[ str, FilePosition ], None, None ] :


   def __repr__( self ) -> str : 
      return "FileWalker: " + self. topdir 

   def __str__( self ) -> str :
      return "FileWalker: " + self. topdir


