##############
# Kevin Long #
# 014065153  #
# Lab 1      #
##############
import string
alphabet = string.ascii_lowercase   # Global variable for lowercase ASCII alphabet chars

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

if __name__ == '__main__':
    """
    Takes user input and calls the functions to do their jobs.
    """
    # User input section
    user = str(input("Enter a sentence: "))
    message = user.split(' ')
    
    code = str(input("Would you like to encode(E) or decode(D) the sentence? "))
    coding = code.upper()

    shift = int(input("What is the shift? "))
    print() # Space before printing

    if coding == "E":
        enigma = translate(message, shift)
    elif coding == "D":
        enigma = translate(message, shift * -1)
        
    enigmaMachine(enigma)   # Calls function to print the final message


