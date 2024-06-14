def word_to_hex(word):
    hex_list = []
    for char in word:
        hex_value = hex(ord(char))
        hex_list.append(hex_value)
    return hex_list

def handler():
    input_word=input("Insert a word: ")
    hex_list = word_to_hex(input_word)
    print("Hexadecimal representation of each character in the word: ", hex_list)
    counter=0
    suspiciousChars=[]
    for char in hex_list:
        for key, value in hexDict.items():
            for node in value:
                if char == node:
                    counter=counter+1
                    suspiciousChars.append(char)
    if counter > 0:
        print("\nWARNING!!!!\n\nThese are the suspicious chars: ",suspiciousChars)
    else:
        print("\nNo suspicious chars!")

hexDict={
    "a": [
        "0x430",
        "0x0e0",
        "0x0e1",
        "1xea1",
        "0x105"
    ],
    "c": [
        "0x441",
        "0x188",
        "0x10b"
    ],
    "d": [
        "0x501",
        "0x257"
    ],
    "e": [
        "0x435",
        "1xeb9",
        "0x117",
        "0x117",
        "0x0e9",
        "0x0e8"
    ],
    "g": [
        "0x121"
    ],
    "h": [
        "0x4bb"
    ],
    "i": [
        "0x456",
        "0x0ed",
        "0x0ec",
        "0x0ef"
    ],
    "j": [
        "0x458",
        "0x29d"
    ],
    "k": [
        "0x3ba"
    ],
    "l": [
        "0x4cf",
        "1xe37"
    ],
    "n": [
        "0x578"
    ],
    "o": [
        "0x43e",
        "0x3bf",
        "0x585",
        "0x22f",
        "1xecd",
        "1xecf",
        "0x1a1",
        "0x0f6",
        "0x0f3",
        "0x0f2"
    ],
    "p": [
        "0x440"
    ],
    "q": [
        "0x566"
    ],
    "s": [
        "0x282"
    ],
    "u": [
        "0x3c5",
        "0x57d",
        "0x0fc",
        "0x0fa",
        "0x0f9"
    ],
    "v": [
        "0x3bd",
        "0x475"
    ],
    "x": [
        "0x445",
        "0x4b3"
    ],
    "y": [
        "0x443",
        "0x0fd"
    ],
    "z": [
        "0x290",
        "0x17c"
    ]
}
handler()
