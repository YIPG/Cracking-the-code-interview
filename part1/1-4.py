# 回文にできるかは文字数が偶数のときそれぞれの文字出現回数cが2|c(偶数回)であることが必要十分
# 文字数が奇数のときはc = oddとなるようなcが一つ。その他は2|cであることが必要十分。
# たぶん回答はASCII想定なので、ここでは言語は英語、コードはASCIIとする。アルファベットずるすぎンゴ

import unittest


def palindrome(string):
    string = string.lower()
    counter = [0 for _ in range(128)]
    if len(string) % 2 == 0:
        for char in string:
            pos = ord(char)
            counter[pos] += 1
        for count in counter:
            if count % 2 == 1:
                return False
        return True
    else:
        for char in string:
            pos = ord(char)
            counter[pos] += 1
        odd_counter = 0
        for char in counter:
            if char == 1:
                odd_counter += 1
        return(odd_counter == 1)


text = "wasi hah siwa"
print(palindrome(text))


class Test(unittest.TestCase):
    data = [
        ("I love evole ei ", True),
        ("Tomato", False),
        ("Tomamto", True),]
        ("wasi hah siwa", True)]
    # data = [
    #     ('Tact Coa', True),
    #     ('jhsabckuj ahjsbckj', True),
    #     ('Able was I ere I saw Elba', True),
    #     ('So patient a nurse to nurse a patient so', False),
    #     ('Random Words', False),
    #     ('Not a Palindrome', False),
    #     ('no x in nixon', True),
    #     ('azAZ', True)]

    def test_palindrome(self):
        for [test_string, torf] in self.data:
            result = palindrome(test_string)
            self.assertEqual(result, torf)


if __name__ == "__main__":
    unittest.main()
