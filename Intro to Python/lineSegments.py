''' 

This module contains a set of functions
which produce and return text line segments.

Each function returns a str of 5 characters.

These are the four strs that are returned:

XXXXX
-----
=====
      (line of five space characters)

                   Author: Mandrake Alscace
Date of last modification: 2014.02.14
           Copyright 2014: What Slefto PolyTech

'''

LINE_SEGMENT_LENGTH = 5

def line_segment_of_spaces( ):
    '''
        return short space character segment
    '''
    return ' ' * LINE_SEGMENT_LENGTH 

def line_segment_of_Xs( ):
    '''
        return short X character segemnt,
    '''
    return 'X' * LINE_SEGMENT_LENGTH 

def line_segment_of_hyphens( ):
    '''
        returns short - character segemnt
    '''
    return '-' * LINE_SEGMENT_LENGTH 

def line_segment_of_equals( ):
    '''
        returns short = character segemnt
    '''
    return '=' * LINE_SEGMENT_LENGTH 
