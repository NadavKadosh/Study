# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    stack = []
    placesstack = []
    for i in range(len(text)):
        n = len(stack) - 1
        if text[i] in ["(", "[", "{"]:
            stack.append(text[i])
            placesstack.append(i+1)
        else:
            if text[i] in [")", "]", "}"] and len(stack) != 0 :
                if text[i] == ")" and stack[n] != "(" or text[i] == "]" and stack[n] != "[" or text[i] == "}" and stack[n] != "{":
                    return False , i+1
                else:
                    if text[i] in [")", "]", "}"]:
                        stack.pop()
                        placesstack.pop()
            elif text[i] in [")", "]", "}"] and len(stack) == 0:
                return False, i+1
    if len(stack) != 0:
        return False, placesstack[len(placesstack)-1]
    else:
        return True, 0





def main():
    text = input()
    mismatch , place = find_mismatch(text)
    if mismatch:
        print("Success")
    else:
        print(place)


if __name__ == "__main__":
    main()
