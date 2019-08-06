import argparse
import sys

def getOptions( args = sys.argv[2:] ):
    parser = argparse.ArgumentParser( description = "Parses commands." )
    parser.add_argument( "-i", "--input", help = "Input file." )
    parser.add_argument( "-a", "--append", help = "Message to be appended to file." )

    options = parser.parse_args( args )
    return options


class TermColors:
    BOLD = '\033[1m'
    RED = '\033[91m'
    ENDL = '\033[0m'

class Book:

    def __init__( self, fileName ):
        self.holdData = []

        try:                # In case the file is already created
            with open( fileName ) as fbuf:
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
            with open( fileName, 'w' ) as fbuf:
                fbuf.write( 'prueba.prueba' + '\n' )
                fbuf.write( '--' )

    def checkEx( self, nameFile ):
        # Error raised in case the file does not exist in fileName
        auxCounter = 0
        for group in self.holdData:
            if nameFile in group:
                auxCounter += 1
        if auxCounter == 0:
            raise ValueError( 'ERROR: The file does not exist in .book' )
        else:
            pass

    def finData( self, nameFile ):
        # Find the data to print the content out in the command line
        self.checkEx( nameFile )    # Check existence of the file
        for group in self.holdData:
            if nameFile in group:
                for elem in group:
                    print( TermColors.RED + TermColors.BOLD + elem + TermColors.ENDL ) \
                            if elem == group[0] else None
                    print( TermColors.BOLD + elem + TermColors.ENDL ) \
                            if elem != '--' and elem != group[0] else None

    def appData( self, nameFile, comment ):
        # Append data to the last position in the group
        self.checkEx( nameFile )    # Check existence of the file
        for i in range( len( self.holdData ) ):
            if self.holdData[i][0] == nameFile:
                self.holdData[i].pop( -1 )
                self.holdData[i].append( comment )
                self.holdData[i].append( '--' )

    def elmData( self, nameFile, line ):
        # Eliminate data to a group depending of type of argument
        self.checkEx( nameFile )    # Check existence of the file
        try:
            line = int( line )
            for i in range( len( self.holdData ) ):
                if nameFile in self.holdData[i]:
                    self.holdData[i].pop( line + 1 )
        except ValueError:
            for i in range( len( self.holdData ) ):
                if nameFile in self.holdData[i]:
                    auxHold = []
                    for stat in self.holdData[i]:
                        if line not in stat:
                            auxHold.append( stat )
                    self.holdData[i] = auxHold
                    auxHold = []    # Just in case there are more matches

    def flsData( self ):
        with open( fileName, 'w' ) as fbuf:
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
    book = Book( fileToSave )

    # Manage the IO with external commands
    # book.finData( nameFile )

    # Test the parser


