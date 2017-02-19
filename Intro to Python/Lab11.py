#!C:/python27/python.exe
'''
Kenneth Huynh N18178828
This program is for rec11.
'''
from __future__ import print_function

STARTUP_FILE_NAME = "wordsWordsWords.txt"

def startUpFillWordList( wordList ):
    ''' opens wordsWordsWords.txt and fills list with words from that file
        the words in that file are one per line
		words in the list must not contain any newline character
    '''
    print( "LIST WOULD BE FILLED WITH WORDS FROM FILE")
    fileHandle = open('lab11words.txt', 'r')
    for word in fileHandle:
        wordList.append(word)
    return wordList
    fileHandle.close()
    

def saveWords( wordList ):
    ''' Store current word list into the file: wordsWordsWords.txt
	    This will destroy the previous version of the file without
		making a backup.
		words are stored one per line.
	'''
    print( "WORDS WOULD BE SAVED HERE" )
    fh = open(STARTUP_FILE_NAME, 'w')
    for word in fh:
        fh.write(word)
    fh.close()

def makeHTMLfile( wordList ):
    ''' makes file: _________.html using words in wordList '''
    print( "HTML FILE WOULD BE CREATED HERE" )
    fileName = raw_input('What is the file name? (end with .html please!)')
    title = raw_input('What is the title?')
    htmlstr = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'''
    titlestr = '<title>' + title + '</title>'
    htmlstr += titlestr
    htmlstr += '''</head>
<body>'''
    for x in wordList:
        htmlstr += x
    htmlstr += '''</body>
</html>'''
    
    fh = open(fileName,'w')
    fh.write(htmlstr)

	
def getValidStartupFilename( ):
    ''' returns the user's choice of filename
	    filename must have .clrs, .csv or .unx extension
    '''
    print( "WOULD GET VALID STARTUP FILENAME HERE" )


    
def getOneWord( prompt ):
    ''' prompts user with passed in prompt then  
	    enforces that the user types only 
		one word on the line
	    and returns that one word
    '''
    word = raw_input( prompt )
    while len( word.split() ) != 1:
        word = raw_input( "Just one word! Try again: " )
    return word

def addWord( wordList ):
    ''' adds user's input word to wordList '''
    word = getOneWord( "Enter word to add: " )
    if word not in wordList:
        wordList.append( word.strip() )
    else:
        print( "%s rejected - already in list" % word )

	# teachy note:
	#        if not not wordList:
	# directly tests for empty string

    
def removeWord( wordList ):
    ''' removes user's choice of word from list if it is there '''
    if len( wordList ) == 0:
        print( "currently no words, can't remove" )
        return
    wordToChunk = getOneWord( "Which word to remove? " )
    try:
        wordList.remove( wordToChunk )
    except ValueError:
        print( wordToChunk + " is not in current list of words" )
    except:
        print( "Serious error has occured. Program is bailing out!" )
        exit( -1 )

       
def showWords( wordList ):
    ''' display each word in current set, one per line '''
    if len( wordList ) == 0:
        print( "currently no words" )
        return
    print( "Your words are:" )
    for word in wordList:
        print( word )
		
		
		
# Global constants used in menu system		

MENU_CHOICE_VALUE_POSTITION = 0
MENU_CHOICE_TEXT_POSTITION = 1
SHOW_CUR_WORDS = ( 1, "1. Display current words" )
ADD_WORD       = ( 2, "2. Add word to current list (will not allow duplicates)" )
REMOVE_WORD    = ( 3, "3. Remove word form current list" )
MAKE_HTML_FILE = ( 4, "4. Print an HTML version of words in current list (under construction)" )
SAVE_AND_EXIT  = ( 5, "5. Save current list and exit" )
MENU = ( SHOW_CUR_WORDS, ADD_WORD, REMOVE_WORD, MAKE_HTML_FILE, SAVE_AND_EXIT )
VALID_MENU_VALUE_CHOICES = ( SHOW_CUR_WORDS[ MENU_CHOICE_VALUE_POSTITION ], \
                             ADD_WORD[ MENU_CHOICE_VALUE_POSTITION ], \
                             REMOVE_WORD[ MENU_CHOICE_VALUE_POSTITION ], \
                             MAKE_HTML_FILE[ MENU_CHOICE_VALUE_POSTITION ], \
                             SAVE_AND_EXIT[ MENU_CHOICE_VALUE_POSTITION ] )
QUIT_CHOICE = SAVE_AND_EXIT[ MENU_CHOICE_VALUE_POSTITION ] - 1
         
def displayMenu():
    ''' prints menu on screen '''
    print( "\n\nrec11 MENU\nPlease choose from the following:\n" )
    for menuLine in MENU:
        print( menuLine[ MENU_CHOICE_TEXT_POSTITION ] )

def getValidMenuChoice():
    ''' returns a valid menu choice '''
    displayMenu()
    choice = raw_input( "Enter menu choice (just the number, please): " )
    while not choice.isdigit() \
          or \
          int(choice) not in VALID_MENU_VALUE_CHOICES:
        print( "Not a valid menu choice." )
        displayMenu()
        choice = raw_input( "Enter menu (just the number, please): " )
    return int( choice ) - 1

def handleMenuChoice( choice, wordList ):
    ''' calls function to handle a valid menu choice
        assumes choice is valid
    '''
    print( )

    if   MENU[ choice ] == ADD_WORD:
        addWord( wordList )
        
    elif MENU[ choice ] == REMOVE_WORD:
        removeWord( wordList )
        
    elif MENU[ choice ] == MAKE_HTML_FILE:
        makeHTMLfile( wordList )
        
    elif MENU[ choice ] == SHOW_CUR_WORDS:
        showWords( wordList )
        
    elif MENU[ choice ] == SAVE_AND_EXIT:
        saveWords( wordList )
        print( "Your words are saved in file " + STARTUP_FILE_NAME )
        print( "Thanks for using this program" )
        
    else: # SERIOUS PROBLEM
        print( "program is exiting due to menu error" )
        exit( 1 )

def getAndHandleMenuChoice( wordList ):
    ''' processes wordList based on menu choice '''
    mChoice = getValidMenuChoice()
    handleMenuChoice( mChoice, wordList )
    return mChoice    
    
def main():

    print( )
    print( )

    wordList = [ ]
    wordList = startUpFillWordList( wordList )
    print(wordList)

    menuChoice = getAndHandleMenuChoice( wordList )
    while menuChoice != QUIT_CHOICE:
        menuChoice = getAndHandleMenuChoice( wordList )

    print( )
    print( )

# are we being executed?
if __name__ == '__main__':
    main()
