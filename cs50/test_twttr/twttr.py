def main():
    word = input("input: ")
    new_word = shorten(word)
    print(new_word)


def shorten(word):
    vowel_rmv_table = (str.maketrans("", "", "aeiouAEIOU"))
    word = word.translate(vowel_rmv_table)
    return word



if __name__ == "__main__":
    main()





