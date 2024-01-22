class SuperStr(str):

    def is_repeatance(self, s):
        if not isinstance(s, str):
            return False
        n = len(self) // (len(s) or 1)
        return self == n * s

    def is_palindrome(self):
        s = self.lower()
        return s == s[::-1]


sup = SuperStr('123123123123')
sup.is_repeatance('123')
print(sup.is_repeatance('123'))
sup.is_repeatance('1234')
print(sup.is_repeatance('1234'))

sup = SuperStr('12399321')
print(sup.is_palindrome())
sup = SuperStr('12398321')
print(sup.is_palindrome())


#task5