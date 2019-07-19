#!/usr/bin/python

"""
Author: wellthisishere
Version: 1.0
About: Enumeration of challenge. 
submit answers for the hacking site www.trytodecrypt.com
"""

import argparse
import urllib.request

parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key", help = "login key for api")
parser.add_argument("--id", help = "id of challenge found in challenge url")
parser.add_argument("-i", "--input", help = "input a string to be encypted and see output")
args = parser.parse_args()

"""
The varible is a url used to interact with the api each one with concatenated 
with the login key for the api.
"""

IdUrl = '&id='+args.id
EncryptUrl = 'http://api.trytodecrypt.com/encrypt?key='+args.key+IdUrl

"""
function for enumeration it create a url for each letter avaible for input
then apped a key and value to a dictionary of translations
"""
def Enumeration(Input):
    Url = EncryptUrl+'&text='+''.join(Input) 
    response = urllib.request.urlopen(Url)
    EncryptedText = response.read()
    EncryptedText = EncryptedText.decode('utf-8')
    Enum.update({Input: EncryptedText})

if __name__=='__main__':
    """
    Input for algorithm enumeration. The website says these are the only valid charaters
    """
    AlphaNumOther = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c',
                    'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '%20', '_', '.',
                    ',', ';', ':', '?', '!']
    Enum = dict()
    
    if args.input:
        Enumeration(args.input)
        for k, v in Enum.items():
            print('Input:\t', k)
            print('Output:\t', v)
    else: 
        for char in AlphaNumOther:
            Enumeration(char)
        EnumFile = open("Enumeration.txt","w")
        for k, v in Enum.items():
            EnumFile.write("{} {}\n".format(k, v))
        EnumFile.close
