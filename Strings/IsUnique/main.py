def isUnique(string: str) -> bool:
    seenChars = {}
    for char in string:
        if seenChars.get(char):
            return False
        else: seenChars[char] = True
    return True

def main():
    print("Are they unique?\n-------")
    string1 = "abcdefg"
    string2 = "this work"
    string3 = "this breaks"
    string4 = "sssa"
    print(string1, isUnique(string1))
    print(string2, isUnique(string2))
    print(string3, isUnique(string3))
    print(string4, isUnique(string4))

if __name__ == "__main__":
    main()
