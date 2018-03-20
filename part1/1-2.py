# ２つの文字列をS1, S2とする。
# ソートして比較

# 解法1: 文字列をリストにしてソート。比較。


def p_string1(S1, S2):
    S1_l = list(S1)
    S2_l = list(S2)
    if len(S1) != len(S2):
        return False
    elif S1_l.sort() == S2_l.sort(): # TODO: はいここが駄目。アルファベットと数字が混ざるとソートできないからエラーになる。
        return True

# p_string("dog ", "g od") > OK!

# 解法2: 出現回数をカウント
# ここではcounterモジュールを使わずに辞書を用いて実装する


def p_string2(S1, S2):
    if len(S1) != len(S2):
        return False
    counter = {}  # 辞書をつくる
    for string in S1:
        if string in counter:  # 辞書は持っていないキーを指定して演算するとエラーを起こすので、キーを持っているか確認が必要
            counter[string] += 1
        else:
            counter[string] = 1
    for string in S2:
        if string not in counter:  # 辞書は持っていないキーを指定して演算するとエラーを起こすので、キーを持っているか確認が必要
            return False
        if counter[string] == 0:
            return False
            counter[string] -= 1
        return True

# TODO: Test書きたい。
# text1="dogrun"
# text2="godnur"
# print(p_string1(text1,text2))
# print(p_string2(text1,text2))

# 2018/3/16追記
# 上の書き方はいけてない。
import unittest
class test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )
    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = p_string2(*test_strings)
            self.assertTrue(result)
        #false check
        for test_strings in self.dataF:
            result = p_string2(*test_strings)
            self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
