import ascii

# returns input text as nul terminated binary string
def t2b(text):
    bin = "0000011000010101"
    i = 0
    while i < len(text):
        char = text[i]
        if char == '\\':
            i += 1
            char += text[i]
            bin += ascii.a2b[text[i]]
            i += 1
        else:       
            bin += ascii.a2b[text[i]]
            i += 1
    bin += ascii.a2b['NUL']
    return bin

def b2t(binary):
    text = ""
    i = 0
    while i < len(binary):
        b = binary[i:i + 8]
        if i < 16:
            if i == 0 and b != '00000110':
                print("This file does not appear to have an encoded message from the first byte.")
                return 
            if i == 8 and b != '00010101':
                print("This file does not appear to have an encoded message from the second byte.")
                return                 
        else:
            if b != '00000000':
                text += ascii.b2a[b]
            else:
                return text
        i += 8
