#!/usr/bin/python

"""
Author: wellthisishere
Version: 1.0
About: sending an solutions and solves problem
submit answers for the hacking site www.trytodecrypt.com
"""

import argparse
import urllib.request

parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key", help = "login key for api")
parser.add_argument("--id", help = "id of challenge found in challenge url")
parser.add_argument("-c", "--challenge", help = "text to decrypt for challenge")
args = parser.parse_args()

"""
The next two vaible create a url used to send the 
"""

IdUrl = '&id='+args.id
SolveUrl = 'http://api.trytodecrypt.com/solve?key='+args.key+IdUrl

"""
chops the challenge to the appropriate length chunk and looks up each chunk value
and returns the key. in the end provides the plaintext
"""
if __name__=='__main__':
    solution = ''
    Enum = {}
    EnumDict = open("Enumeration.txt","o")
    for line in EnumDict:
        (key, val) = line.split()
        Enum[int(key)] = val
    print(Enum)
    Enum[' '] = Enum.pop('%20')
    print("solution: ", end='')
    if args.id != '6':
        challenge = [challenge[i:i+2] for i in range(0, len(challenge), 2)]
    elif args.id == '8':
        challenge = [challenge[i:i+3] for i in range(0, len(challenge), 3)]
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
