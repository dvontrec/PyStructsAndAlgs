def checkPermutation(string1: str, string2: str) -> bool:
    if len(string1) != len(string2):
        return False
    seenChars = {}
    for i in range(len(string1)):
        char1 = string1[i]
        char2 = string2[i]
        if not seenChars.get(char1):
            seenChars[char1] = 0
        if not seenChars.get(char2):
            seenChars[char2] = 0
        seenChars[char1] += 1
        seenChars[char2] -= 1

    for key in seenChars:
        if seenChars[key] != 0:
            return False

    return True


def main():
    print("Are they permutations?\n-----")
    string1 = "aabbc"
    string2 = "abcba"
    string3 = "unrelated"
    string4 = "something"
    string5 = "wont"
    string6 = "succeed"
    print(string1, string2, checkPermutation(string1, string2))
    print(string3, string4, checkPermutation(string3, string4))
    print(string5, string6, checkPermutation(string5, string6))

if __name__ == "__main__":
    main()
