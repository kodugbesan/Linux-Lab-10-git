import sys

def shift(c, n):
    if c.isalpha():
        shifted = chr(((ord(c) - 65 + n) % 26) + 65)
        return shifted
    else:
        return ""

def main():
    if len(sys.argv) == 2:
        shift_amt = int(sys.argv[1])
        input_str = input("Enter a message: ").upper()
        encoded_str = ""
        i = 0
        for c in input_str:
            encoded_str += shift(c, shift_amt)
            i += 1
            if i % 5 == 0:
                encoded_str += " "
            if i % 50 == 0:
                encoded_str += "\n"
        print(encoded_str)

if __name__ == "__main__":
    main()

