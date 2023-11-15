def main():
    camel_word = input("camelCase: ")
    print(convert_snake(camel_word))


def convert_snake(camel_word):
    new_word = []
    for letter in camel_word:
        if letter.islower():
            new_word.append(letter)
        else:
            new_word.append("_")
            new_word.append(letter.lower())

    return "".join(new_word)


main()
