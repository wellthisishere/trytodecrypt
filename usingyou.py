#!/usr/bin/python

"""
Author: wellthisishere
Version: 1.0
About: trying to solve problem 6 have to rewrite enumeration funciton
submit answers for the hacking site www.trytodecrypt.com
"""

import argparse
import urllib.request

parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key", help = "login key for api")
parser.add_argument("-i", "--id", help = "id of challenge found in challenge url")
parser.add_argument("-c", "--challenge", help = "text to decrypt for challenge")
parser.add_argument("-d", "--dump", help = "dump enum diction to stdout", action="store_true")
args = parser.parse_args()

"""
The next two urls are to interact with the api each one with concatenated 
with the login key since the api does not without it.
"""

IdUrl = '&id='+args.id
EncryptUrl = 'http://api.trytodecrypt.com/encrypt?key='+args.key+IdUrl
SolveUrl = 'http://api.trytodecrypt.com/solve?key='+args.key+IdUrl

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

"""
chops the challenge to the appropriate length chunk and looks up each chunk value
and returns the key. in the end provides the plaintext
"""
def solve(challenge):
    solution = ''
    Enum[' '] = Enum.pop('%20')
    print("solution: ", end='')
    if args.id != '6':
        challenge = [challenge[i:i+2] for i in range(0, len(challenge), 2)]
    else:
        challenge = [challenge[i:i+4] for i in range(0, len(challenge), 4)]
    for x in challenge:
        for k, v in Enum.items():
            if x == v:
                solution += k
    
    print(solution)
    solution = solution.replace(' ', '%20')
    Url = SolveUrl+'&solution='+solution
    response = urllib.request.urlopen(Url)
    check = response.read()
    check = check.decode('utf-8')
    if check == '1':
        print('correct')
    else:
        print('wrong')

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

    for x in AlphaNumOther:
        Enumeration(x)

    if args.dump:
        for k, v in Enum.items():
            print(k, v)
    else:
        solve(args.challenge)
