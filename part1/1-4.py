# 回文にできるかは文字数が偶数のときそれぞれの文字出現回数cが2|c, 偶数回であることが必要十分
# 文字数が奇数のときはc = oddとなるようなcが一つ。その他は2|cであることが必要十分。
# たぶん回答はASCII想定なので、ここでは言語は英語、コードはASCIIとする。アルファベットずるすぎンゴ

import unittest


def palindrome(string):
    counter = [0 for _ in range(128)]
    if len(string) % 2 == 0:
        for char in string:
            pos = ord(char)
            counter[pos] += 1
        for count in counter:
            if count%2==1:
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

text="abcdeffedcba"
print(palindrome(text))
