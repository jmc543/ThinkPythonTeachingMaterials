def first(word):
    return word[0];


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

if __name__ == '__main__':
    print(is_palindrome('justin'))  # False
    print(is_palindrome('bob'))  # True
    print(is_palindrome('random words'))  # False
    print(is_palindrome('amanaplanacanalpanama'))  # True
