#Here I create a simple algorithm for encryption and decryption.
#No insert function in this file.

from ast import Pass
from copy import copy, deepcopy
from hashlib import new
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
    

def decodeletterswapnext(message):
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


#random letter swapping algorithm + decoder
def mixupsymbols(inputlist, seed):
    """
    Mix up the list of symbols for
    use in swaprandomletter.
    """
    letterlist = deepcopy(inputlist)
    rng = random.Random()
    rng.seed(seed)
    newlist = ""
    for i in list(range(len(letterlist))):
        newletter = rng.choice(letterlist)
        newlist += newletter
        letterlist.remove(newletter)
    
    return str(newlist)




def swaprandomletter(message, seed):
    """
    Swaps each letter to another random letter,
    displays also the decryption seed to decode.
    """
    output = ""

    newlist = mixupsymbols(varfiles.ALPHABET, seed)
    newdict = alphabet_number(newlist)

    for letter in message:
        mletindex = varfiles.ENUMALPH[letter]
        output += newdict[mletindex]
    
    return """Encrypted message "{0}" with seed {1} """.format(output, seed)
        

def decodeswaprandomletter(message, seed):
    """
    Decodes a message encrypted by swaprandomletter.
    Requires the same seed as in swaprandomletter.
    """
    output = ""

    newlist = mixupsymbols(varfiles.ALPHABET, seed)
    numdict = number_alphabet(newlist)

    for letter in message:
        letindex = numdict[letter]
        originaletter = varfiles.NUMLETT[letindex]
        output += originaletter
    
    return """Decrypted message "{0}" from seed {1} """.format(output, seed)


#full algorithm swaps random symbol
def swaprandom(message, seed=None):
    """
    Swaps each letter to another random symbol,
    displays also the decryption seed to decode.
    No whitespace allowed!
    """
    output = ""
    if seed == None:
        rng = random.Random()
        seed = rng.randint(0, 10**100)

    newlist = mixupsymbols(varfiles.ALLSYMBOLS, seed)
    newdict = alphabet_number(newlist)

    for letter in message:
        mletindex = varfiles.ENUMALL[letter]
        output += newdict[mletindex]
    
    return """Encrypted message >>> {0} <<< with seed {1} """.format(output, seed)
        

def decodeswaprandom(message, seed):
    """
    Decodes a message encrypted by swaprandom.
    Requires the same seed as in swaprandom.
    No whitespace allowed!
    """
    output = ""

    newlist = mixupsymbols(varfiles.ALLSYMBOLS, seed)
    numdict = number_alphabet(newlist)

    for letter in message:
        letindex = numdict[letter]
        originaletter = varfiles.NUMALL[letindex]
        output += originaletter
    
    return """Decrypted message >>> {0} <<< from seed {1} """.format(output, seed)



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
        decodeletterswapnext("bcdvvviuza") == "abcuuuhtyz"
    )



    #generation of lists and dictionaries
    print("Here is the alphabet enumerated \n {0}".format(
        number_alphabet(varfiles.ALPHABET)
    ))

    print("Here are numbers corresponding to letters \n {0}".format(
        alphabet_number(varfiles.ALPHABET)
    ))

    print(
        list(string.punctuation)
    )
    
    print("Here is the symbol list keyed with symbols:\n {0}".format(
        number_alphabet(list(string.ascii_letters + string.punctuation + string.digits))
    ))

    print("Here is the symbol list keyed with numbers:\n {0}".format(
        alphabet_number(list(string.ascii_letters + string.punctuation + string.digits))
    ))

    print("Here is a list of all symbols:\n {0}".format(
        list(string.ascii_letters + string.punctuation + string.digits)
    ))




    print("Full list keyed with symbols enum:\n {0}".format(
        number_alphabet(list(string.ascii_letters + string.punctuation + string.digits + string.whitespace))
    ))

    print("Full list keyed with numbers num:\n {0}".format(
        alphabet_number(list(string.ascii_letters + string.punctuation + string.digits + string.whitespace))
    ))

    print("Full list of all symbols used:\n {0}".format(
        list(string.ascii_letters + string.punctuation + string.digits + string.whitespace)
    ))


    #main algorithms displayed
    print(
        letterswapnext("")
    )
    print(
        decodeletterswapnext("fhhqmbou")
    )

    print(
        mixupsymbols(['a', 'b'], 1126)
    )
    
    print(
        mixupsymbols(varfiles.ALPHABET, 1126)
    )
    
    print(
        swaprandomletter("eggplant", 1126)
    )

    print(
        decodeswaprandomletter("myyfwive", 1126)
    )

    print(
        swaprandom("""Oh,ElisabethMyRegina.FormulaeOf#$789ipsum!oneAreDisplayed.""", 1126)
    )

    print(
        decodeswaprandom("""m+Xp,dJIiNA+"=}N`d9IY[Muz4,INmOW'(jnd)J4z!M9NfuN>dJ),I=NcY""", 1126)
    )
    