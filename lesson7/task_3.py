str_list = ["abccba", "123", "dadadad", "lol", "321123"]


def is_palindrome(word):
    return word.lower() == word[::-1].lower()


print(list(filter(is_palindrome, str_list)))

print(list(filter(lambda x: x.lower() == x[::-1].lower(), str_list)))
