def is_anagram(word1, word2):
    list1 = list(word1)
    list2 = list(word2)
    list1.sort()
    list2.sort()
    return list1 == list2

if __name__ == '__main__':
    w1 = "silent"
    w2 = "listen"
    w3 = "potato"
    print(is_anagram(w1, w2))
    print(is_anagram(w1, w3))
