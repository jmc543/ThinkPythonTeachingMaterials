# one-liner to check if a word is a palindrome
def is_palindrome(word):
    return word == word[::-1]

if __name__ == '__main__':
    # testing:
    print(is_palindrome("abcdcba"))
    print(is_palindrome("not a palindrome"))
