# ポインタつくって動かしていけばええんちゃうか？
# 英語だったらASCII想定で、リストのインデックスと対応させる。日本語だったらUTF8想定で辞書つくったほうがいい。
# 3/24追記。それだめや。aabbaaだとa2b2a2がa4b2となってまう。
import unittest

#
# def zip_string(string):
#     sl = list(string)
#     count_list=[0 for _ in range(128)]
#     counter = 1
#     for i in range(len(string)):
#         a = sl.pop(i)
#         count_list[ord(a)] +=1
#         if a == sl[i]:
#             count_list[ord(a)] += 1
#         sl=list(string)


def zip_string(string):
    result = ""
    str_result = ""
    count = 1
    for i in range(0, len(string) - 1):
        char = string[i]
        if string[i] == string[i + 1]:
            count += 1
            if i == len(string) - 2:
                result += char + str(count)
        else:
            result += char + str(count)
            count = 1
            if i == len(string) - 2:
                result += string[-1] + str(1)

    str_result = result[0::2]
    if str_result == string:
        return string
    else:
        return result


class Test(unittest.TestCase):
    data = [
        ("aaaabbcccd", "a4b2c3d1"),
        ("abcd", "abcd"),
        ("aaabbbFFFkkk", "a3b3F3k3")
    ]

    def test_zip_string(self):
        for [string, answer] in self.data:
            self.assertEqual(zip_string(string), answer)


if __name__ == "__main__":
    unittest.main()
