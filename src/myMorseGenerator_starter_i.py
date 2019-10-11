#!/usr/bin/env python3
"""myMorseGenerator_solution_i.py: Program to use generator functions to put text into morse code."""


DATE = "10 Oct 2019"
VERSION = "i"
AUTHOR = "PLEASE ADD YOUR NAME HERE"
AUTHORMAIL = "@allegheny.edu"

# The dictionary of Morse code. keys = alphabet chars, values = code.
morse_dict = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	      'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',
              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',  ' ':'/'     ,  '.':'.-.-.-',
              ',':'--..--',  ':':'---...',  '?':'..--..',
              "'":'.----.',  '-':'-....-',  '/':'-..-.',
              '@': '.--.-.', '=':'-...-',   '(':'-.--.',
              ')':'-.--.-',  '+':'.-.-.',   '!':'-.-.--',
              ';':'-.-.-'
        }

def help():
        h_str = "   "+DATE+" | version: "+VERSION+" |"+AUTHOR+" | "+AUTHORMAIL
        print("  "+len(h_str) * "-")
        print(h_str)
        print("  "+len(h_str) * "-")
        print("\n\tA Morse encoder and decoder program.")
        #print("""\n\tLibrary installation notes:""")
        print("\t+ \U0001f600  USAGE: programName <any key to launch>")
#end of help()



def myMorseEncoder(msg_str):
    """ function to create a generator to yield each letter in morse code"""
    print("\t myMorseEncoder()")
    out_str = ""
    for i in msg_str:
    #    print(" myMorsegen() :",i)
        out_str = out_str + morse_dict[i.upper()] + " "
    #    print ("myMorseGen, out_str = ",out_str)
    yield out_str
#end of myMorseEncoder()


#end of myMorseEncoder()

def myMorseDecoder(msg_str):
    """ function to decode the morse code into the original text characters"""
    print("\t myMorseDecoder()")

##################################################################################################################
# TODO: Morse Code characters to text characters
# Complete the code: Lookup the text character (keys)
# using morse_dict from their associated Morse code values.
# Be sure to apply generators to this function.
##################################################################################################################

#end of myMorseDecoder()

def isMorseCode(in_str):
    """ Function to determine whether the input is code or text"""
    # are only the chars of the morse code alphabet in the string?
    if len(Counter(in_str)) <= 4 and "-" in in_str or "." in in_str or "/" in in_str:
        return True
    else:
        return False
#end isMorseCode()

def begin():
    """Driver function"""
    msg_str = input('\t Input your message (text or encoded) : ')
    out_str = ""
    if isMorseCode(msg_str) != True:
        for i in msg_str:
            print("  ",i," : ",morse_dict[i.upper()])
        print("\t Generator component: encoding")
        out_str = myMorseEncoder(msg_str)

    else: # is morse code
        print("\t Generator component: decoding")
        out_str = myMorseDecoder(msg_str)
    print("\t Type :",type(out_str))
    print("\t Message: ",next(out_str))
#end of begin()

from collections import Counter
import sys

if __name__ == '__main__':

    if len(sys.argv) == 2: # one parameter at command line
    # note: the number of command line parameters is n + 1
            begin()#,sys.argv[2])#,sys.argv[3], sys.argv[4]),sys.argv[5])
    else:
            help()
            sys.exit()
