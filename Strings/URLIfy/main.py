def urlify(s: str, trueLength: int) -> str:
    s = [c for c in s]
    pointer1 = trueLength -1
    pointer2 = len(s) - 1
    while pointer1 >= 0:
        if s[pointer1] == " ":
            s[pointer2] = "0"
            pointer2 -= 1
            s[pointer2] = "2"
            pointer2 -= 1
            s[pointer2] = "%"
        else: s[pointer2] = s[pointer1]
        pointer1 -= 1
        pointer2 -= 1

    return "".join(s)


def main():
    print("URLifying...\n-----")
    string1 = "Test This Out    "
    string2 = " Python strings are immutable        "
    print(string1, urlify(string1, 13))
    print(string2, urlify(string2, 29))

if __name__ == "__main__":
    main()
