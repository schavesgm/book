
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
                # appData( 'prueba.prueba', self.holdData, 'Esto es lo que se debe de hacer' )
                # finData( 'prueba.prueba', self.holdData )
        except IOError:     # In case the file does not exist
            with open( fileName, 'w' ) as fbuf:
                fbuf.write( 'prueba.prueba' + '\n' )
                fbuf.write( '--' )

def checkEx( nameFile, holdData ):
    # Error is raised in case the file does not exist in file
    if nameFile not in holdData:
        raise ValueError( 'ERROR: The file does not exist' )
    else:
        pass

def finData( nameFile, holdData ):
    # Find the data to print it out in the command line
    for group in holdData:
        if nameFile in group:
            for elem in group:
                print( elem ) if elem !=  '--' else None

def appData( nameFile, holdData, comment ):
    # Append data to the last position in the group
    for i in range( len( holdData ) ):
        if holdData[i][0] == nameFile:
            holdData[i].pop( -1 )
            holdData[i].append( comment )
            holdData[i].append( '--' )


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


