import os
import urllib.request
import random


URL = 'https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt'
FILE_NAME = URL.split('/')[-1]


def download_wordlist():
    '''Download the EFF wordlist if not there already'''
    if not os.path.isfile(FILE_NAME):
        print('Downloading EFF large wordlist ...')
        urllib.request.urlretrieve(URL, FILE_NAME)


def get_words():
    '''Turn the EFF file into a dict'''
    with open(FILE_NAME, 'r') as i:
        lines = i.read().splitlines()
        phrase_dict = dict([x.split('\t') for x in lines])
    return phrase_dict


def get_passphrase(phrase_dict):
    '''Generate the passphrase'''
    
    def get_dice_numbers():
        '''Get a random string of 5 dice numbers'''
        num = ''
        for _ in range(0, 5):
            num += str(random.randint(1, 6))
        return num

    # get a list of five 5-digit dice numbers
    word_list= [get_dice_numbers() for _ in range(0, 5)]
    
    # return a space-delimited string of the corresponding words from the EFF list
    return ' '.join([phrase_dict[x] for x in word_list])


if __name__ == '__main__':
    download_wordlist()
    phrase_dict = get_words()
    passphrase = get_passphrase(phrase_dict)
    print(passphrase)
