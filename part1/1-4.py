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
        if counter % 2 == 0:
            return True
        else:
            return False
    else:
        for char in string:
            pos = ord(char)
            counter[pos] += 1
        odd_counter=0
        for char in counter:
            if char ==1:
                odd_counter+=1
        if odd_counter==1:
            return True
        else:
            return False
