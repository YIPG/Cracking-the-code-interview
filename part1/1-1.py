import unittest

# ある文字列をSとする
# 言語は日本語、文字コードはUnicode (日本語3byte)を想定

# 解法1: O(N^2)


def unique(S):
    if len(S) > 2**24:
        return False
    for index in range(len(S)):
        if S[index] in S[index + 1:]:
            return False
            break
        elif index == len(S) - 1:
            return True

# 解法2: 時間はO(N)だが、2^24の長さのリストをつくるのでメモリを喰うゾイ
def unique2(S):
    if len(S) > 2**24:
        return False
    char_set=[False for _ in range(2**24)]
    for char in S:
        uni_num=ord(char)
        if char_set[uni_num]:
            return False
        char_set[uni_num] = True
    return True

class Test(unittest.TestCase):
    dataT = [("こんにちは"), ("わたしは"), ("ぺっぱーです")]
    dataF = [("ようよう"), ("おれさまのなまえは"), ("じゃいあんだぜい")]

    def test_unique(self):

        for test_string in self.dataT:
            torf = unique(test_string)
            self.assertTrue(torf)

        for test_string in self.dataF:
            torf = unique(test_string)
            self.assertFalse(torf)


if __name__ == "__main__":
    unittest.main()
