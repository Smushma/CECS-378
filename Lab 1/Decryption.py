##############
# Kevin Long #
# 014065153  #
# Lab 1      #
##############
import string
alphabet = string.ascii_lowercase   # Global variable for lowercase ASCII alphabet chars

#-----CAESAR CIPHER-----
def translate(message, shift):
    """
    Takes a list of words, iterates through, and passes each word to encode function.
    Takes the value returned by encode function and adds it the the newMessage list.
    @input message: list of strings
    @return: the new list
    """
    newMessage = [] # new list
    for i in range(len(message)):
        newWord = encode(message[i], shift) # sends to encode func
        newMessage.append(newWord)

    return newMessage

def encode(word, shift):
    """
    Takes an individual word and iterates through each character
    @param word: the current word in list
    @param shift: how much to shift
    @return: the edited word
    """
    encoded_word = ""   
    word = word.lower()
    for char in word:   # iterate thru the chars to match ascii alphabet
        if char not in alphabet:
            encoded_word += char
        else:
            alphaIndex = alphabet.index(char)
            if alphaIndex + shift >= 26:
                alphaIndex = (alphaIndex + shift) % len(alphabet)
                encoded_word += alphabet[alphaIndex]
            elif alphaIndex + shift < 0:
                alphaIndex = ((alphaIndex + shift) % len(alphabet))
                encoded_word += alphabet[alphaIndex]
            else:
                encoded_word += alphabet[alphaIndex + shift]
                
    return encoded_word

def enigmaMachine(enigma):
    """
    Prints the final edited message.
    @param enigma: list of words
    """
    for i in range(len(enigma)):    # Iterates thru the list and properly formats it for printing.
        for j in range(len(enigma[i])):
            print(enigma[i][j], end = "")
        print(" ", end = "")
    print()

def bruteForceCaesar(message):
    """
    Iterates through all the possible shifts in the alphabet.
    @param message: the message to decrypt in string format
    """
    msgToDecrypt = message.split(' ')
    for shift in range(1, 26):
        print("Shift:", shift)
        enigma = translate(msgToDecrypt, shift * -1)
        enigmaMachine(enigma)
        print()

#-----LETTER ANALYSIS-----
import operator

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ETAOIN = 'etaionshrdlcumwfgypbvkjxqz' #How often eng chars appear in descending order

#For letter frequency reference
engLetterFreq = {'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97,
                 'n': 6.75, 's': 6.33, 'h': 6.09, 'r': 5.99, 'd': 4.25,
                 'l': 4.03, 'c': 2.78,'u': 2.76, 'm': 2.41, 'w': 2.36,
                 'f': 2.23, 'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29,
                 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15, 'q': 0.10,
                 'z': 0.07}

def letterAnalysis(message):
    """
    Attempts to decipher a message based on letter frequency.
    @param message: the message to decrypt in string format
    """
    msg = message #message.replace(" ", "")
    #Counts how often a letter appears in the msg
    msgLetterFreq = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
                     'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
                     'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
                     'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
                     'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
                     'z': 0}

    for letter in msg: #Count the num of times a letter appears in msg
        if letter in ALPHABET:
            msgLetterFreq[letter] += 1
            
    #Orders the letters based on times appeared (descending order)
    sortedLetterFreq = sorted(msgLetterFreq.items(), key=lambda x: x[1], reverse=True)
    
    freqConv = {} #Dict to match msgLetterFrequency to ETAOIN
    for i in range(0, 26):
        freqConv[sortedLetterFreq[i][0]] = ETAOIN[i] #Matches the msgLetterFreq(key) to ETAOIN order(value)

    result = ''
    for char in msg:
        if char != ' ':
            result += freqConv[char]
        else:
            result += ' '
        
    print("Letter freq. in message:\n" + str(sortedLetterFreq))
    print()
    print("Mapping based on ETAOIN:\n" + str(freqConv))
    print()
    print("Decryption:\n" + result)

if __name__ == '__main__':
    decode = str(input("Would you like to decode via Caesar Cipher(C) or Letter Analysis(L)? "))
    decoding = decode.upper()

    if decoding == "C": 
        message = str(input("Enter a sentence: "))
        bruteForceCaesar(message)

    elif decoding == "L":
        message = str(input("Enter a sentence: "))
        letterAnalysis(message)
    
    #-----FOR TESTING PURPOSES-----
    #-----Caesar Cipher-----
    #msg1 = 'fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc' #-----SHIFT 9-----
    #bruteForceCaesar(msg1)
    
    #msg2 = 'oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy' #-----SHIFT 21-----
    #bruteForceCaesar(msg2)

    #-----Letter Analysis-----
    #msg3 = 'ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae'
    #letterAnalysis(msg3)

    #msg4 = 'iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq iihed yzhni ifnun sayiz yudhe sqshu qesqa iluym qkque aqaqm oejjs hqzyu jdzqa diesh niznj jayzy uiqhq vayzq shsnj jejjz nshna hnmyt isnae sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun siiqa suoij qqfni syyle iszhn bhmei squih nimnx hsead shqmr udquq uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz'
    #letterAnalysis(msg4)
