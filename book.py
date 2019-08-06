
class Book():

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
                self.finData( 'prueba.prueba' )
                self.appData( 'prueba.prueba', 'Esto es lo que se debe de hacer' )
                self.appData( 'prueba.prueba', 'Y lo hacemos a escondidas' )
                self.finData( 'prueba.prueba' )
                self.flsData( )
                # print( self.holdData )
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
                    print( elem ) if elem != '--' else None

    def appData( self, nameFile, comment ):
        # Append data to the last position in the group
        self.checkEx( nameFile )    # Check existence of the file
        for i in range( len( self.holdData ) ):
            if self.holdData[i][0] == nameFile:
                self.holdData[i].pop( -1 )
                self.holdData[i].append( comment )
                self.holdData[i].append( '--' )

    def flsData( self ):
        with open( fileName, 'w' ) as fbuf:
            for group in self.holdData:
                for elem in group:
                    fbuf.write( elem + '\n' )
# holdData = []
# try:                # In case the file is already created
#     with open( fileName ) as fbuf:
#         contents = fbuf.readlines()
#         contents = [ x.strip() for x in contents ]
#         # Hold the data into holdData
#         auxHold = []
#         for line in contents:
#             auxHold.append( line )
#             if line == '--':
#                 holdData.append( auxHold )
#                 auxHold = []
#         appData( 'prueba.prueba', holdData, 'Esto es lo que se debe de hacer' )
#         finData( 'prueba.prueba', holdData )
#
#
# except IOError:     # In case the file does not exist
#     with open( fileName, 'w' ) as fbuf:
#         fbuf.write( 'prueba.prueba' + '\n' )
#         fbuf.write( '--' )

if __name__ == '__main__':

    # File to save the data
    fileName = '.book'

    # Create a Book object that will manage the IO
    book = Book( fileName )


