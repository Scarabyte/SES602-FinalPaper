#######################
#    CyberSecurity    #
#    Caesar Cipher    #
#    Adam Burbidge    #
#######################

# Specify a shift amount to use
SHIFT_AMOUNT = 3


def caesar_cipher(message, shift):
    """Simple substitution cipher, selectable shift amount"""
    output = ""
    for token in message:
        # Normalize to zero and shift upper case characters
        if token.isupper():
            output = output + chr(((ord(token) - ord("A")
                                    + shift) % 26) + ord("A"))
        # Normalize to zero and shift lower case characters
        elif token.islower():
            output = output + chr(((ord(token) - ord("a")
                                    + shift) % 26) + ord("a"))
        else:
            output = output + token
    return(output)


def viginere(message, codeword):
    """Substitution cipher, using a codeword for the shift amount"""
    output = ""
    for idx, token in enumerate(message):
        # Take only alpha characters
        if codeword[idx % len(codeword)].isalpha():
            # Take only upper case characters
            if codeword[idx % len(codeword)].isupper():
                shift = ord(codeword[idx % len(codeword)]) - ord("A")
            # Take only lower case characters
            elif codeword[idx % len(codeword)].islower():
                shift = ord(codeword[idx % len(codeword)]) - ord("a")
            else:
                # No character shift otherwise
                shift = 0
        output = output + caesar_cipher(token, shift)
    return output


if __name__ == '__main__':
    message_plain = input("Input your message: ")

    print(caesar_cipher(message_plain, SHIFT_AMOUNT))
    print(viginere("message", "WORD"))
