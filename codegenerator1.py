#Here I create a simple algorithm for encryption and decryption.
#No insert function in this file.

from ast import Pass
import string
import varfiles
import random
from testfile import test

#the following two functions are used to obtain dictionaries of the alphabet.
def number_alphabet(letterlist):
    """Enumerates a list or a string; 
    returns a dictionary with keys as symbols."""
    enumletters = {}
    for i, letter in enumerate(letterlist):
        enumletters[letter] = i
    
    return enumletters


def alphabet_number(letterlist):
    """Enumerates a list or a string;
    returns a dictionary with keys as index numbers."""
    numletters = {}
    for i, letter in enumerate(letterlist):
        numletters[i] = letter
    
    return numletters


#here lies the first algorithm for encoding and
#decoding a message. A simple next letter.
def letterswapnext(message):
    """Encrypts a letter-only message by
    changing each letter to the next. Only 
    small letters possible. Returns a string."""
    output = ""
    for letter in message:
        letindex = varfiles.ENUMALPH[letter]
        #statement for looping back too large indices
        if letindex + 1 < len(varfiles.NUMLETT):
            newletindex = letindex + 1
        else:
            newletindex = letindex + 1 - len(varfiles.NUMLETT) #undecodable if >0 (impossible here)

        newletter = varfiles.NUMLETT[newletindex]
        output = output + newletter
    
    return output
    

def nextletterunswap(message):
    """Takes an encoded message by next letter
    swap and turns it back to the original
    message."""
    output = ""
    for letter in message:
        letindex = varfiles.ENUMALPH[letter]
        #statement for looping back 0
        if letindex != 0:
            newletindex = letindex - 1
        else:
            newletindex = max(varfiles.NUMLETT) #largest key

        newletter = varfiles.NUMLETT[newletindex]
        output = output + newletter
    
    return output



if __name__ == "__main__":
    #tests
    test(
        number_alphabet(['b', 'g', 'h']) == {'b': 0, 'g': 1, 'h': 2} 
    )
    test(
        alphabet_number(['b', 'g', 'h']) == {0: 'b', 1: 'g', 2: 'h'}
    )
    test(
        letterswapnext("abcuuuhtyz") == "bcdvvviuza"
    )
    test(
        nextletterunswap("bcdvvviuza") == "abcuuuhtyz"
    )



    #main
    print("Here is the alphabet enumerated \n {0}".format(
        number_alphabet(varfiles.ALPHABET)
    ))

    print("Here are numbers corresponding to letters \n {0}".format(
        alphabet_number(varfiles.ALPHABET)
    ))

    print(
        letterswapnext("eggplant")
    )
    print(
        nextletterunswap("fhhqmbou")
    )

