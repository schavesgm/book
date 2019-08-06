import argparse
import sys

def getOptions( args = sys.argv[1:] ):
    parser = argparse.ArgumentParser( description = "Parses commands." )

    msgInp = 'Input file.'
    msgApp = 'Message to be appended to the file.'
    msgDel = 'Delete the nth comment of a file or the lines containing string.'
    msgRem = 'Remove all the contents related to a file'
    msgAll = 'Show all the files registered'

    parser.add_argument( "-i", "--input", help = msgInp )
    parser.add_argument( "-a", "--append", help = msgApp )
    parser.add_argument( "-d", "--delete", help = msgDel )
    parser.add_argument( '-r', '--remove', help = msgRem )
    parser.add_argument( '-S', '--show_all', help = msgAll, action = 'store_true' )

    parser.set_defaults( show_all = False )

    options = parser.parse_args( args )
    return options


class TermColors:
    BOLD = '\033[1m'
    RED = '\033[91m'
    ENDL = '\033[0m'

class Book:

    def __init__( self, fileToSave, nameFile ):

        self.holdData = []
        self.fileToSave = fileToSave
        self.nameFile = nameFile

        try:                # In case the file is already created
            with open( fileToSave ) as fbuf:
                contents = fbuf.readlines()
                contents = [ x.strip() for x in contents ]
                # Hold the data into holdData
                auxHold = []
                for line in contents:
                    auxHold.append( line )
                    if line == '--':
                        self.holdData.append( auxHold )
                        auxHold = []
        except IOError:     # In case the file does not exist
            with open( fileToSave, 'w' ) as fbuf:
                fbuf.write( 'prueba.prueba' + '\n' )
                fbuf.write( '--' )

    def checkEx( self ):
        # Error raised in case the file does not exist in fileName
        auxCounter = 0
        for group in self.holdData:
            if self.nameFile in group:
                auxCounter += 1
        if auxCounter == 0:
            raise ValueError( 'ERROR: The file does not exist in .book' )
        else:
            pass

    def finData( self ):
        # Find the data to print the content out in the command line
        self.checkEx()    # Check existence of the file
        for group in self.holdData:
            if self.nameFile in group:
                for elem in group:
                    print( TermColors.RED + TermColors.BOLD + elem + \
                           TermColors.ENDL ) \
                            if elem == group[0] else None
                    print( TermColors.BOLD + elem + TermColors.ENDL ) \
                            if elem != '--' and elem != group[0] else None

    def shwData( self ):
        # Show all the data registered
        for group in self.holdData:
            for elem in group:
                print( TermColors.RED + TermColors.BOLD + elem + \
                       TermColors.ENDL ) \
                        if elem == group[0] else None
                print( TermColors.BOLD + elem + TermColors.ENDL ) \
                        if elem != '--' and elem != group[0] else None


    def appData( self, comment ):
        # Append data to the last position in the group
        self.checkEx()    # Check existence of the file
        for i in range( len( self.holdData ) ):
            if self.holdData[i][0] == self.nameFile:
                self.holdData[i].pop( -1 )
                self.holdData[i].append( comment )
                self.holdData[i].append( '--' )

    def elmData( self, line ):
        # Eliminate data to a group depending of type of argument
        self.checkEx()    # Check existence of the file
        try:
            line = int( line )
            for i in range( len( self.holdData ) ):
                if self.nameFile in self.holdData[i]:
                    self.holdData[i].pop( line + 1 )
        except ValueError:
            for i in range( len( self.holdData ) ):
                if self.nameFile in self.holdData[i]:
                    auxHold = []
                    for stat in self.holdData[i]:
                        if line not in stat:
                            auxHold.append( stat )
                    self.holdData[i] = auxHold
                    auxHold = []    # Just in case there are more matches

    def delFile( self ):
        # Eliminate the data corresponding to a file
        self.checkEx()
        for i in range( len( self.holdData ) ):
            if self.nameFile in self.holdData[i]:
                self.holdData.pop( i )

    def flsData( self ):
        with open( self.fileToSave, 'w' ) as fbuf:
            for group in self.holdData:
                for elem in group:
                    fbuf.write( elem + '\n' )

if __name__ == '__main__':

    # File to save the data
    fileToSave = '.book'

    # Generate the file name to be used
    if getOptions().input is not None:
        nameFile = getOptions().input
    else:
        nameFile = input( "Enter name of file: " )

    # Create a Book object that will manage the IO
    book = Book( fileToSave, nameFile )

    # Append something to the file
    if getOptions().append is not None:
        book.appData( getOptions().append )

    if getOptions().delete is not None:
        book.elmData( getOptions().delete )

    if getOptions().remove is not None:
        book.delData( )

    if getOptions().show_all:
        book.shwData()

    # Print the data and flush it out
    # book.finData()
    book.flsData()



